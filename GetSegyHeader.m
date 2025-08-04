% GetSegyHeader : Reads the segyheader of a SEG-Y formatted file
% Call: 
%  [SegyHeader]=GetSegyHeader(segyid);%
%  segyid can be a filehandle or a filename

function [SegyHeader]=GetSegyHeader(segyid);

if isstr(segyid)
    % if segyid is a string it is interpreted as a filename
    segyid = fopen(segyid,'r','b');   % ALL DISK FILES ARE IN BIG ENDIAN FORMAT, ACCORDING TO SEG-Y rev 1
end

% Basic Segy Header Information.
SegyHeader.Rev=GetSegyHeaderBasics;

fseek(segyid,0,'bof');
SegyHeader.TextualFileHeader=fread(segyid,3200,'uchar');         % 3200
SegyHeader.Job=fread(segyid,1,'int32');                           % 3204 
SegyHeader.Line=fread(segyid,1,'int32');                          % 3208
SegyHeader.Reel=fread(segyid,1,'int32');                          % 3212
SegyHeader.DataTracePerEnsemble=fread(segyid,1,'int16');        % 3214
SegyHeader.AuxiliaryTracePerEnsemble=fread(segyid,1,'int16');   % 3216
SegyHeader.dt=fread(segyid,1,'uint16');                          % 3218
SegyHeader.dtOrig=fread(segyid,1,'uint16');                      % 3220
SegyHeader.ns=fread(segyid,1,'uint16');                          % 3222
SegyHeader.nsOrig=fread(segyid,1,'uint16');                      % 3224
SegyHeader.DataSampleFormat=fread(segyid,1,'int16');            % 3226
SegyHeader.EnsembleFold=fread(segyid,1,'int16');                
SegyHeader.TraceSorting=fread(segyid,1,'int16');               % 3228
SegyHeader.VerticalSumCode=fread(segyid,1,'int16');            % 3230

SegyHeader.SweepFrequencyStart=fread(segyid,1,'int16');        % 3232
SegyHeader.SweepFrequencyEnd=fread(segyid,1,'int16');          % 3234
SegyHeader.SweepLength=fread(segyid,1,'int16');                % 3236
SegyHeader.SweepType=fread(segyid,1,'int16');                  % 3238
SegyHeader.SweepChannel=fread(segyid,1,'int16');               % 3240
SegyHeader.SweepTaperlengthStart=fread(segyid,1,'int16');               % 3242
SegyHeader.SweepTaperLengthEnd=fread(segyid,1,'int16');               % 3244
SegyHeader.TaperType=fread(segyid,1,'int16');               % 3246

SegyHeader.CorrelatedDataTraces=fread(segyid,1,'int16');               % 3248

SegyHeader.BinaryGain=fread(segyid,1,'int16');               % 3250
SegyHeader.AmplitudeRecoveryMethod=fread(segyid,1,'int16');               % 3252

SegyHeader.MeasurementSystem=fread(segyid,1,'int16');               % 3254

SegyHeader.ImpulseSignalPolarity=fread(segyid,1,'int16');               % 3256
SegyHeader.VibratoryPolarityCode=fread(segyid,1,'int16');               % 3258

% **************************************************************************

% commented on Feb. 21, 2004

% % 3261-3500 UNASSIGNED (as 120*2byte integer)
% SegyHeader.Unassigned1=fread(segyid,120,'int16');               % 3260
% 
% % fseek(segyid,3500,'bof');
% SegyHeader.SegyFormatRevisionNumber=fread(segyid,1,'uint16');   % 3500
% SegyHeader.FixedLengthTraceFlag=fread(segyid,1,'integer*2');        % 3502
% SegyHeader.NumberOfTextualHeaders=fread(segyid,1,'uint16');        % 3504
% 
% % 3506-3600 UNASSIGNED (as 47*2byte integer = 94 byte)
% SegyHeader.Unassigned2=fread(segyid,47,'int16');               % 3260
% 
% 
% 
% 
% % READ TEXTURAL FILE HEADER EXTENSION IF NEEDED
% %fseek(segyid,3600,'bof');
% nChars=3200*SegyHeader.NumberOfTextualHeaders;
% SegyHeader.TextualHeaders=fread(segyid,nChars,'schar');        % 3504

% **************************************************************************

SegyHeader.time=[1:1:SegyHeader.ns].*SegyHeader.dt./1e+6;
if isstr(segyid)
    fclose(segyid);
end
