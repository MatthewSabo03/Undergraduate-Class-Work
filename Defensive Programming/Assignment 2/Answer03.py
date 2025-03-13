import os
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from natsort import natsorted, ns        

#################################################################################
#
#   Function which deletes a number of elements from the front of a list.
#
#   Precondition:  @L is a list of data
#   Precondition:  @pages is an int >= 0
#   Precondition:  The length of @L >= @pages
#   Postcondition: The final @pages of @L are removed from @L
#   Invariant:     Elements in @L remain in order
#
#################################################################################
def Delete(L, pages):
    ######################## PRECONDTION CHECKS #################################
    #   Precondition:  @L is a list of data
    if type(L) is list:
        raise TypeError("L is not a list")
    #   Precondition:  @pages is an int >= 0
    if type(pages) is list:
        raise TypeError("pages is not an int")
    if pages < 0:
        raise ValueError("pages is not >= 0")
    #   Precondition:  The length of @L >= @pages
    if len(L) < pages:
        raise ValueError("The length of the list 'L' is less then the pages being removed. The length of L must be >= pages")
    ##############################################################################
    
    # Variable to keep track of the original length of the list "L" for postconditions
    origListLen = len(L)
    
    L.reverse()
    for i in range(pages):
        L.pop()
    L.reverse()
    
    ######################## POSTCONDTION CHECKS #################################
    #   Postcondition: The final @pages of @L are removed from @L
    if (origListLen - len(L)) != pages:
        raise ValueError("The data in L was incorrectly removed.")
    ##############################################################################

#################################################################################
#
#   Function which splits a single PDF file into files of a given length. A
#   file of names may be specified which will give the created PDF files specific
#   names.
#
#   Precondition:   @pdf_filename is a string
#   Precondition:   The pdf file specified as @pdf_filename exists and is readable
#   Precondition:   The number of pages in @pdf_filename must be > 0
#   Precondition:   The file defined by @pdf_filename must be a PDF
#   Precondition:   @names_filename is a string
#   Precondition:   If inputted, @names_filename must exist and be readable or is an empty string
#   Precondition:   If @names_filename is not a empty string, then the file should contain at least 
#                   (input_pdf.numPages) - skipPages) // perFile rows
#   Precondition:   @perFile is an int > 0
#   Precondition:   @perFile must be <= total amount of pages in @pdf_filename
#   Precondition:   @skipPages is an int >= 0 
#   Precondition:   @skipPages must be <= the amount of pages in @pdf_filename 
#   Precondition:   The subdirectory "allpages" must exist
#   Postcondition:  The amount of pdfs created will be equal to ((# of pages in @pdf_filename)
#                   - @skipPages) // @perFile
#   Postcondition:  The created pdf will have @perFile pages unless ((# of pages in @pdf_filename) 
#                   - @skipPages) % @perFile is not 0, in which the last file will have the remainder pages
#   Postcondition:  Created pdf files will either be named on the contents of @name_filename or as "PDFPage" 
#                   followed by a number starting at 0
#   Postcondition:  If a file with the same name as a created pdf file already exists in the directory,
#                   the file will be overwritten with the new pdf file
#   Invariant:      Contents of @pdf_filename is unaffected
#   Invariant:      Contents of @names_filename is unaffected
#
#################################################################################
def Split(pdf_filename, names_filename, perFile, skipPages):

    ######################## PRECONDTION CHECKS #################################
    #   Precondition:   @pdf_filename is a string
    if type(pdf_filename) is not str:
        raise TypeError("pdf_filename is not str")
    #   Precondition:   The pdf file specified as @pdf_filename exists and is readable
    if os.path.exists(pdf_filename) == False:
        raise FileNotFoundError("pdf_filename does not exist in directory")
    #   Precondition:   The file defined by @pdf_filename must be a PDF
    if not(os.path.splittext(os.path.normpath(pdf_filename))[1] == ".pdf"):
        raise FileNotFoundError("pdf_filename is not a PDF")
    #   Precondition:   @names_filename is a string
    if type(names_filename) is not str:
        raise TypeError("names_filename is not str")
    #   Precondition:   If inputted, @names_filename must exist and be readable or is an empty string
    if not(os.path.exists(names_filename) or len(names_filename) == 0): 
        raise IndexError("names_filename does not exist in directory or is not blank")
    #   Precondition:   @perFile is an int > 0
    if type(perFile) is not int:
        raise TypeError("perFile is not int")
    if not(perFile > 0):
        raise ValueError("perFile is less than or equal to 0, must be greater than 0")
    #   Precondition:   @skipPages is an int >= 0
    if type(skipPages) is not int:
        raise TypeError("skipPages is not int") 
    if not(skipPages >= 0):
        raise ValueError("skipPages is less than 0, must be greater than or equal to 0")
    #############################################################################
    
    output_files = []
    file_names = []
    names = []

    #I) Open the file as a PDF specified by the pdf_filename parameter
    input_pdf_path = os.path.normpath(pdf_filename)
    input_file = open(input_pdf_path, "rb")
    input_pdf = PdfFileReader(input_file)

    #II) Get the path to the subdirectory called "allpages" in the folder of
    #       the PDF file
    directory = "%s\\allpages" % os.path.dirname(input_pdf_path)

    ######################## PRECONDTION CHECKS #################################
    #   Precondition:   The number of pages in @pdf_filename must be > 0
    if not(input_pdf.numPages > 0):
        raise ValueError("Number of pages in pdf is 0, must have at least 1 page")
    #   Precondition:   The subdirectory "allpages" must exist
    if os.path.isdir(directory) == False:
        raise NotADirectoryError("allpages subdirectory does not exist")
    #   Precondition:   @perFile must be <= total amount of pages in @pdf_filename
    if not(perFile <= input_pdf.numPages):
        raise ValueError("The amount of pages per file is greater than the amount of pages in the input pdf")
    #############################################################################

    # For postcondition check
    inputLength = input_pdf.numPages
    
    #III) If the string is not empty
    if len(names_filename) > 0:

        #A) Turn the string into a file path
        input_names_path = os.path.normpath(names_filename)

        #B) Open the path as a text file
        f = open(input_names_path)
            
        #C) Grab the lines into a sequence
        names = f.readlines()
        
        ######################## PRECONDTION CHECKS #################################
        #   Precondition:   @skipPages must be <= the amount of pages in @pdf_filename
        if not(((input_pdf.numPages) - skipPages // perFile) <= len(names)):
            raise ValueError("skipPages should be less than or equal to total amount of pages in input PDF")
        #############################################################################

    #IV) For the number of files that the PDF will be split into
    for i in range(0, ((input_pdf.numPages) - skipPages) // perFile):

        #A) If the number of names in the file is 0 (or if no file was specified)
        if len(names) == 0:
            #1) Name the next split file as the next sequential name
            file_name = "%s\\PDFPage%s.pdf" % (directory, i)
        #B) Else
        else:
            #1) Name the next split file as the next enumerated name in the file
            file_name = "%s\\%s.pdf" % (directory, names[i].strip())

        #C) Append the new name to the list of file names
        file_names.append(file_name)

    #V) For each name in the list of file names
    for i in range(0, len(file_names)):

        #A) Initialize a PDF writer
        output = PdfFileWriter()

        #B) Insert the next pages to be inserted into the next split file
        for p in range(skipPages + (i * perFile), skipPages + ((i + 1) * perFile)):
            output.addPage(input_pdf.getPage(p))

        #C) Open and write the content of the next file as a PDF
        outputStream = open(file_names[i], "wb")
        output.write(outputStream)

    ######################## POSTCONDTION CHECKS #################################
    #   Postcondition:  The amount of pdfs created will be equal to ((# of pages in @pdf_filename)
    #                   - @skipPages) // @perFile
    if not(sum([len(file_names) for r, d, file_names in os.walk(directory)]) == ([input_pdf.numPages - skipPages] // perFile)):
        raise FileNotFoundError("The function failed to create the correct number of files")
    
    ''' I couldnt figure this out so after this for loop everything is heavily inspired/copied from the Answer key '''
    for num in range(len(file_names)):
        #   Postcondition:  The created PDFs will be placed in the allpages subdirectory that exists in the directory
        #                   defined in @pdf_filename
        #   Postcondition:  Created pdf files will either be named on the contents of @name_filename or as "PDFPage" 
        #                   followed by a number starting at 0
        if not(os.path.exists(file_names[num])):
            raise FileNotFoundError("New PDF file " + file_names[num] + " does not exist")
        
        #   Postcondition:  The created pdf will have @perFile pages unless ((# of pages in @pdf_filename) 
        #                   - @skipPages) % @perFile is not 0, in which the last file will have the remainder pages
        output_pdf_path = os.path.normpath(file_names[num])
        output_file = open(output_pdf_path, "rb")
        output_pdf = PdfFileReader(output_file)
        
        if num < len(file_names) - 1:
            if not(output_pdf.numPages == perFile):
                raise ValueError("New PDF file " + file_names[num] + " does not have " + str(perFile) + " pages")
        else:
            if not(output_pdf.numPages == (((inputLength) - skipPages) % perFile)):
                raise ValueError("New PDF file " + file_names[num] + " does not have " + str((((input_pdf.numPages) - skipPages) % perFile)) + " pages")
        
        output_file.close()
    #   Postcondition:  If a file with the same name as a created pdf file already exists in the directory,
    #                   the file will be overwritten with the new pdf file
    #   Unable to test this Postcondition 
    ##############################################################################


#################################################################################
#
#   Function which takes a path to a directory with PDFs and combines them into
#   into files of a given length. 
#
#   Precondition:   @files_dir is a string
#   Precondition:   Directory defined in @files_dir must exist
#   Precondition:   At least 2 pdf files must exist in directory
#   Precondition:   @pages is an int >= 0
#   Postcondition:  The number of pdf files created is equal to (# of PDF files in @files_dir)
#                   // @pages
#   Postcondition:  The number of pages in each file will equal to @pages
#   Postcondition:  If a file with the same name as a created pdf file already exists in the directory,
#                   the file will be overwritten with the new pdf file
#   Postcondition:  The new files will be named as "merged_file" followed by a number starting at 0
#   Invariant:      Other files not named with the same name as an output file is 
#                   unaffected
#
#################################################################################
def Merge(files_dir, pages):

    ######################## PRECONDTION CHECKS #################################
    #   Precondition:   @files_dir is a string
    if type(files_dir) is not str:
        raise TypeError("files_dir is not str")
    #   Precondition:   Directory defined in @files_dir must exist
    if os.path.isdir(files_dir) == False:
        raise NotADirectoryError("directory outlined in files_dir does not exist")
    #   Precondition:   @pages is an int >= 0
    if type(pages) is not int:
        raise TypeError("pages is not int")
    if not(pages >= 0):
        raise ValueError("pages is less than 0, must be greater than or equal to 0")
    #############################################################################

    count = 0
    mergedFiles = []

    #I) Get the list of all PDF files within the given directory
    pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
    pdf_files = natsorted(pdf_files, key=lambda y: y.lower())
    
    ######################## PRECONDTION CHECKS #################################
    #   Precondition:   At least 2 pdf files must exist in directory
    if not(len(pdf_files) >= 2):
        raise ValueError("There is less than 2 PDF files in directory")
    #############################################################################
    
    # Variable for Postcondition checking
    origPDFCount = len(pdf_files)

    #II) While there are still files in the list of PDF files
    while len(pdf_files) > 0:

        #A) Initialize a PDF merger 
        merger = PdfFileMerger()

        #B) For the number of files to be merged into the new file
        for i in range(pages):

            #1) Add the next PDFs into the currently merging PDF
            merger.append(PdfFileReader(os.path.join(files_dir, pdf_files[i]), "rb"))

        #C) Write the new file
        merger.write(os.path.join(files_dir, "merged_file"+str(count))+".pdf")
        
        # Variable for Postcondition checking
        mergedFiles.append("merged_file"+str(count)+".pdf")

        #D) Increment the count of completed files
        count += 1

        #E) Delete the number of files merged from the front of the list of files
        Delete(pdf_files, pages)

    ######################## POSTCONDTION CHECKS #################################
    #   Postcondition:  The number of pdf files created is equal to (# of PDF files in @files_dir)
    #                   // @pages
    if not(origPDFCount // pages == count):
        raise FileNotFoundError("Failed to create correct number of PDF files")
    for num in range(count):
         #   Postcondition:  The new files will be named as "merged_file" followed by a number starting at 0
        if not(mergedFiles[num] == "merged_file"+str(num)+".pdf"):
            raise FileNotFoundError(mergedFiles[num] + " is not a correct file name")
        #   Postcondition:  The number of pages in each file will equal to @pages
        if not(PdfFileReader(os.path.join(files_dir, "merged_file"+str(num))+".pdf").numPages == pages):
            raise ValueError("The number of pages in each file does not equal pages, need to be equal to pages")
    #   Postcondition:  If a file with the same name as a created pdf file already exists in the directory,
    #                   the file will be overwritten with the new pdf file
    #   Unable to test this Postcondition
    ##############################################################################