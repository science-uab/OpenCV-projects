OpenCV projects

Roboti inteligenti

Nume:  Iga (Voronianu) Sanda  Florina

Master PABD anul I 2018

###Descriere:
Programul  realizează  citirea  și   afisarea  unei imagini din folderol proiectului.

#include <opencv2/core/core .hpp>

#include <opencv2/highgui/highgui .hpp>

Declararea   fisierelor de tip include OpenCV.

 Mat imread(const string& filename , int flags=1)
 
Incarca  o imagine de pe disc.

filename: numele fisierului imagine; 

flags: indicator de incarcare a tipului de imagine:

–	CV LOAD_IMAGE ANYDEPTH: incarcă o imagine pe 16-biti \32-biti  atunci  cand  imaginea  corespunde acestor rezolutii, altfel converteste imaginea la 8-biti;

–	CV_LOAD_IMAGE_COLOR: intotdeauna  incarcă   imaginea color;

–	CV_LOAD_IMAGE_GRAYSCALE: converteste imaginea in niveluri de gri; 

–	 < 0: incarca imaginea  asa cum este.

 void namedWindow(const string& winname , int flags=WINDOW_AUTOSIZE)
 
Creaza  o fereastra.
winname: numele ferestrei;

 flags: indicator a tipului de   fereastra:
 
– CV WINDOW AUTOSIZE: dimensiunea ferestrei este setata in functie de dimensiunea imaginii.

 void imshow(const string& winname , InputArray mat)
 
Afiseaza  o imagine  intr-o  fereastra  data:
winname: numele ferestrei; mat: imaginea de intrare.
 int waitKey(int delay=0)
 
Asteapta  ca o tasta sa  fie apasata:
delay:  intarzierea  in milisecunde (0 reprezinta   asteptare infinita).

Rezultatul  executării aplicației.

![alt text](https://github.com/vorosanda/OpenCV-projects/blob/master/Iga_Sanda_proiect_opencv/captura%20opencv.jpg "Printscreen")

