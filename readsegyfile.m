function seismic_data= readsegyfile(filename)
%   union SI si;//采样点数 
%   union SP sp;//定义采样率 
%   union Data data;//定义数据 
%   union Line line;//线号 
%   union Trace trace;//道号 
%   union X_cor x_cor;//X坐标 
%   union Y_cor y_cor;//Y坐标 
%   Line_num     /最大线号 
%   Trace_num    /最大道号 
fid=fopen(filename,'r'); 
   if ~fid 
   { 
       disp('can''t open file!'); 
       exit; 
   } ;
   end 
  fseek(fid,3220,'bof');  %读取采样点数 
  SI=fread(fid,1,'int16','b') ;
  fseek(fid,3216,'bof');  %读取采样率 
  SP=fread(fid,1,'int16','b') ;
  fseek(fid, 0, 'eof'); %计算总文件字节数 
  file_n=ftell(fid); 
  Tn =(file_n-3600)/(SI*4+240) ; %计算道数 
  fclose(fid);  
 seismic_data=zeros(SI,Tn);   
 fid=fopen(filename,'r'); 
   if ~fid 
   { 
       disp('can''t open file!'); 
       exit; 
   } ;
   end 
   for j=1:Tn 
%读取线号 
      fseek(fid,3600+(j-1)*240+(j-1)*SI*4+8,'bof');  
      Line=fread(fid,1,'int32','b'); 
     if j==1 
         Line_first=Line; 
     end 
%读取道号 
      fseek(fid,3600+(j-1)*240+(j-1)*SI*4+20,'bof');  
      Trace=fread(fid,1,'int32','b'); 
     if j==1 
         Trace_first=Trace; 
     end 
%读取X坐标	 
      fseek(fid,3600+(j-1)*240+(j-1)*SI*4+72,'bof');  
%读取Y坐标	 
      fseek(fid,3600+(j-1)*240+(j-1)*SI*4+76,'bof');  
%读取地震数据 
      fseek(fid,3600+j*240+(j-1)*SI*4,'bof');  
      seismic=fread(fid,[1,SI],'float32','b'); 
      seismic_data(:,j)=seismic'; 
   end 
fclose(fid);  
end