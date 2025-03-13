% Prerequisite definitions
% Logic works CLASS -> PREREQ
% CISC 100
prereq('CISC 100', 'Two years of high school algebra or equivalent').
% CISC 140
prereq('CISC140', 'CISC120').
% CISC 160
prereq('CISC160', 'CISC120').
prereq('CISC160', 'CISC140').
% CISC 211
prereq('CISC211', 'CISC120').
% CISC 225
prereq('CISC225', 'CISC120').
% CISC 233
prereq('CISC233', 'CISC160').
% CISC 301
prereq('CISC301', 'CISC211').
prereq('CISC301', 'CISC233').
% CISC 325
prereq('CISC325', 'CISC233').
prereq('CISC325', 'MATH310').
% CISC 333
prereq('CISC333', 'CISC233').
% CISC 340
prereq('CISC340', 'CISC233').
prereq('CISC340', 'MATH310').
% CISC 349
prereq('CISC349', 'CISC225').
prereq('CISC349', 'CISC233').
% CISC 380
prereq('CISC380', '60 Credit Hours Completed').
prereq('CISC380', 'Consent from instructor and academic advisor').
% CISC 390
prereq('CISC390', 'CISC120').
prereq('CISC390', 'CISC140').
prereq('CISC390', '60 Semester Hours Completed').
% CISC 397
prereq('CISC397', 'CISC225').
prereq('CISC397', 'CISC301').
% CISC 399
prereq('CISC399', 'CISC225').
prereq('CISC399', 'CISC301').
% CISC 400
prereq('CISC400', 'CISC120').
prereq('CISC400', 'MATH250').
% CISC 411
prereq('CISC411', 'CISC301').
prereq('CISC411', 'CISC399').
% CISC 431
prereq('CISC431', 'CISC399').
% CISC 432
prereq('CISC432', 'MATH280').
prereq('CISC432', '60 Semester Hours Completed').
% CISC 435
prereq('CISC435', 'CISC340'). 
prereq('CISC435', 'MATH250').
% CISC 460
prereq('CISC460', 'CISC225').
prereq('CISC460', 'MATH310').
% CISC 491
prereq('CISC491', 'CISC397').
% CISC 495
prereq('CISC495', 'CISC298').
prereq('CISC495', 'Permission').
% CISC 498
prereq('CISC498', 'CISC298').
% CISC 499
prereq('CISC499', 'Senior Status').
% MATH 210
prereq('MATH210', 'MATH120').
prereq('MATH210', 'MATH220').
% MATH 220
prereq('MATH220', 'MATH120').
prereq('MATH220', 'MATH140').
prereq('MATH220', 'MATH280').
% MATH 250
prereq('MATH250', 'MATH220').
prereq('MATH250', 'MATH120').
% MATH 310
prereq('MATH310', 'MATH210').
prereq('MATH310', 'MATH260').

% Rule
required(X, Y) :- prereq(X, Z), required(Z, Y).
required(X, Y) :- prereq(X, Y).
