function tracedata=GetSegyTraceData(segyid,ns,SegyHeader,SkipData)
%
% Get Segy Trace Data. 
%
%
if exist('segyid')==0
    disp([filename,' : SEGYID not specified - exiting'])
    tracedata=[];
    return
end
if exist('ns')==0
    disp([filename,' : NS not specified - exiting'])
    tracedata=[];
    return
end
if exist('SegyHeader')==0 , 
    SegyHeader.DataFormat='float32'; 
    SegyHeader.BytesPerSample=32;
    SegyHeader.DataSampleFormat=5; % IEEE
    disp(['Dataformat not specified -  dataformat->',DataFormat.DataFormat])
end;

if exist('SkipData')==0, SkipData=0; end

Revision=SegyHeader.SegyFormatRevisionNumber;
if Revision>0, Revision=1; end
Format=SegyHeader.Rev(Revision+1).DataSampleFormat(SegyHeader.DataSampleFormat).format;  

BPS=SegyHeader.Rev(Revision+1).DataSampleFormat(SegyHeader.DataSampleFormat).bps;  
if (SkipData==1)
    SkipBytes=ns*BPS/8;
    fseek(segyid,SkipBytes,'cof');
    tracedata=[];
else  
    % disp([mfilename,' : ',Format,'. ns=',num2str(ns)])
    try 
      tracedata=fread(segyid,ns,Format);
    catch
      disp([mfilename,' : Error using fread - Possibly ''ns'' is negative -' ...
	    ' check byteorder-'])
      tracedata=[];
    end
    
    
    if (strcmp(Format,'uint32')==1), % IBM FLOATING POINT
        % CONVERT FROM FLOATING POINT
        verbose=1;
        if verbose>1, disp([mfilename,'Converting from IBM, DataFormat :',SegyHeader.DataFormat]); end
        try
          tracedata=ibm2num(uint32(tracedata));
        catch
          % disp([mfilename,' : SOMETHING BAD HAPPENED WHEN CONVERTING FROM IBM FLOATS TO IEEE. ARE YOU SURE DATA ARE IBM FLOAT FORMATTED ?' ])
          % tracedata=0.*tracedata;
          % return

        end
    end;
    
end
