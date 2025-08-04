% ReadSegy : Reads a SEG-Y formatted file

function Data=ReadSegy(filename);

if ~(exist(filename)==2)
  disp([mfilename,' : ', filename,' does not exist !'])  
 return
end

% OPEN FILE HANDLE
segyid = fopen(filename,'r'); 

% BINARY HEADERS
SegyHeader=GetSegyHeader(segyid);

% Revision=SegyHeader.SegyFormatRevisionNumber;
% 2004.02.21
Revision=0;

Format=SegyHeader.Rev(Revision+1).DataSampleFormat(SegyHeader.DataSampleFormat).format;  
BPS=SegyHeader.Rev(Revision+1).DataSampleFormat(SegyHeader.DataSampleFormat).bps; 
ns=SegyHeader.ns;                                   

% READ DATA
fseek(segyid,0,'eof'); 

DataEnd=ftell(segyid);
% DataStart=3600+3200*SegyHeader.NumberOfTextualHeaders;
% 2004.02.21
DataStart=3600;     

fseek(segyid,DataStart,'bof');       % Go to the beginning of the file

ntraces=(DataEnd-DataStart)/(240+ns*(BPS/8));
% disp(['Number of Samples Per Trace=',num2str(SegyHeader.ns)])
% disp(['Number of Traces=',num2str(ntraces)]) 

traceinfile=0;
while (~(ftell(segyid)>=DataEnd))
  traceinfile=traceinfile+1;  
  TraceStart=ftell(segyid);  
  SingleSegyTraceHeaders=GetSegyTrace(segyid,TraceStart);    
  SegyData(traceinfile).data=fread(segyid,ns,Format);   
end

% MOVE DATA from SegyData.data to a regular variable
Data=zeros(ns,traceinfile);
 for i=1:traceinfile   
     Data(:,i)=SegyData(i).data;    
 end 

 %figure,imagesc(Data);colormap(gray);


  
