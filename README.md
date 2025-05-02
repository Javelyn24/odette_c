{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue233;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c0\c0\c93333;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa321\partightenfactor0

\f0\b\fs48 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 ODETTE - Satellite Tracking Core Library\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 Python bindings for the C++ core library of the ODETTE project, providing satellite tracking, orbit determination, and propagation functionality.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Features\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f1\b0\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 TLE parsing and SGP4 propagation\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Orbit determination from optical observations (RA/Dec)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Advanced orbit propagation with various perturbation models\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Frame transformations (ECEF, ECI)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 TDM file parsing\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Orbital mathematics utilities\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Installation\
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf0 Prerequisites\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0
\f1\b0\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 CMake (>= 3.12)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 C++ compiler with C++17 support\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Python (>= 3.6)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Eigen3\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 pybind11\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa280\partightenfactor0

\f0\b\fs28 \cf0 Building from source\
\pard\pardeftab720\partightenfactor0

\f2\b0\fs26 \cf0 # Clone the repository\
git clone https://github.com/yourusername/odette.git\
cd odette\
\
# Install using pip\
pip install .\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Usage Example\
\pard\pardeftab720\partightenfactor0

\f2\b0\fs26 \cf0 import numpy as np\
from odette import satellite_core as sc\
\
# Parse a TLE\
tle = sc.TwoLineElement()\
sc.parse_tle_lines(tle, \
    "1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927",\
    "2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537")\
\
# Get position and velocity\
r = np.zeros(3)\
v = np.zeros(3)\
sc.get_rv(tle, 0.0, r, v)  # At TLE epoch\
print(f"Position: \{r\} km")\
print(f"Velocity: \{v\} km/s")\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Documentation\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 For detailed documentation, please refer to the {\field{\*\fldinst{HYPERLINK "https://github.com/yourusername/odette/wiki"}}{\fldrslt \cf3 \ul \ulc3 \strokec3 project wiki}}.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 License\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 This project is licensed under the MIT License - see the LICENSE file for details.\
}