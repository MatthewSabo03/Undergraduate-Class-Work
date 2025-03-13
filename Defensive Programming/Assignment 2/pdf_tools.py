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
    L.reverse()
    for i in range(pages):
        L.pop()
    L.reverse()


#################################################################################
#
#   Function which splits a single PDF file into files of a given length. A
#   file of names may be specified which will give the created PDF files specific
#   names.
#
#################################################################################
def Split(pdf_filename, names_filename, perFile, skipPages):

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

    #III) If the string is not empty
    if len(names_filename) > 0:

        #A) Turn the string into a file path
        input_names_path = os.path.normpath(names_filename)

        #B) Open the path as a text file
        f = open(input_names_path)
            
        #C) Grab the lines into a sequence
        names = f.readlines()

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


#################################################################################
#
#   Function which takes a path to a directory with PDFs and combines them into
#   into files of a given length. 
#
#################################################################################
def Merge(files_dir, pages):

    count = 0

    #I) Get the list of all PDF files within the given directory
    pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
    pdf_files = natsorted(pdf_files, key=lambda y: y.lower())

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

        #D) Increment the count of completed files
        count += 1

        #E) Delete the number of files merged from the front of the list of files
        Delete(pdf_files, pages)

