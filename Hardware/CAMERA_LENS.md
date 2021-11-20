# Picking Lenses and Sensors

| Model      | Resolution   | Pixel Size      |  Sensor Area      |  Ratio   | Sensor Size      |
|------------|--------------|-----------------|-------------------|----------|------------------|
| OV2640     | 1600 x 1200  |  2.2um x 2.2um  |  3590um x 2684um  |  1.337   |     1/4"      |
| OV5640     | 2592 x 1944  |  1.4um x 1.4um  |  3673um x 2738um  |  1.3414  |     1/4"      |
| OV4689     | 2688 x 1520  |  2.0um x 2.0um  |  5440um x 3072um  |  1.7708  |     1/3"      |
| OV2735     | 1080p        |  3.0um x 3.0um  |  5808um x 3288um  |  1.7662  |     1/2.7"       Package: 6956um x 4765um      |
| OV2732     | 1080p        |  2.0um x 2.0um  |  3868um x 2190um  |  1.7662  |     1/4"      |
| OV2718     | 1080p        |  2.8um x 2.8um  |  5482um x 3202um  |  1.7230  |     1/2.9"      |
| OV2740     | 1080p        |  1.4um x 1.4um  |  2729um x 1550um  |  1.7606  |     1/6"        Lens chief ray angle: 33deg      |
| AR0237     | 1080p 60fps  |  3.0um x 3.0um  |                   | 1/2.7"   | HiSPI ?, 3D support, slave support, 4x4 RGB-IR, AR0237IRSH12SHRA0-DR |

## Lens Requirements

We are looking for a lens for a dual camera system. Lens alone or Lens + Base.

* Horizontal FoV Angle: 110 - 125 deg
* Aperture/Focal: F2.0/4.3mm (or effective range 20cm - 200cm)
* Socket: M7 or M8
* TTL limit: 15 mm, ideally 10 mm
* Sensor lens size: 1/4" - 1/3" 

* [Fuzhou Chuangan](https://chancctv.en.alibaba.com/productgrouplist-804927292/M6_M7_M8_M10_Lens.html)
* [F1.8 M12 mount 3.6mm fixed iris lens for 1/3″ OV4689](https://aico-lens.com/product/3-6mm-megapixel-fixed-focal-lens-ac13b03618mm/)

Pinhole. 140 deg FoV. 1/2.5" sensor. Max 14mm TTL. Ideal focus range 20cm - 200cm. I think F2.0/4.3mm works.


https://dofsimulator.net/en/

https://www.photopills.com/calculators/dof


The New A-25H-D0
Variable Focus Liquid Lens
https://www.corning.com/worldwide/en/products/advanced-optics/product-materials/corning-varioptic-lenses/A-25H-D0_variable_focus_liquid_lens.html
The new A-25H-D0 liquid lens keeps the same clear aperture (2.5mm) but features a wider dynamic range (70D vs. 18D)


Lens requirement


- Perfect focus 25cm - 100cm distance
- Decent focus 20cm - 400cm
- Resolution 3MP
- Sensor size 1/2.5"
- Aperture 2.4
- DFOV 140°+
- M8 or M12. 

Lens holder base requirement

- low profile
- M8 or M12
- Space for 9mm x 9mm physical sensor size
- TTL ~14 mm
- No ears (ideally)


Working assumption:


Aimed at OV2732

Hyperfocal distance 31cm
DoF near limit 24cm

Firefly FOV D70°H62°V38°


## Lenses for testing

| Model           | Manufactur. | Res.   | Type     | Mount    | Sensor   | HFoV | Aperture | Focal   | Bk Focal | Optcl ln  | M.O.D  |Dimensions / Weight   | 
|-----------------|-------------|--------|----------|----------|----------|------|----------|---------|----------|-----------|--------|----------------------|
| M12-1.56MM-5MP  | TREEYE      | 5.0MP  | Fisheye  | M12x0.5  | 1 / 2.5" | 185° | F2.0     | 1.56mm  | 4.3mm    | 20.7mm    | 0.1m   | Dia. 20* 16mm, 12g, $5, IR | 
| M12-2.1MM-5MP-B | TREEYE      | 5.0MP  | Fisheye  | M12      | 1 / 2.5" | 160° | F2.0     | 2.1mm   | 6.9mm    | 20.7mm    | 0.2m   | Φ17.517.5, 8g, $4.2 | 
|                 | AIRFORTH    | ? MP   | Wide     | M8       | 1 / 3"   | 160° |          | 2.1mm   |          |           |        | Racing Drone $3.75 |
| MTV-0368BF127M7 | Lenspro     | 2 MP   | Semi Wide| M7       | 1 / 2.7" | 97°  | F2.8     | 3.68mm  | 2.01mm   |           | 0.3m   | TTL 9.9mm, Φ10x8.6mm, ~9%, FoV 97°/86.5°/50.5° |
| FS2825SCBP      | Focusafe    | ? MP   | Pinhole  | M12x0.5  | 1 / 3"   | 125° | F2.5     | 2.8mm   |          |           | 0.3m   |  F.O.V. 125°*82°*56° |
| FS3725SBP       | Focusafe    | ? MP   | Ph. screw| M12x0.5  | 1 / 3"   | 92°  | F2.5     | 3.7mm   |          |           | 0.2m   |  5g |
| FS3725CBP       | Focusafe    | ? MP   | Pinhole  | M12x0.5  | 1 / 3"   | (95)°| F2.5     | 3.7mm   |          |           | 0.3m   |  6*7.54(mm) |
| CCL127028PMP    | TOWIN       | 3 MP   | Pinhole  | M12x0.5  | 1 / 2.7" | 108° | F2.4     | 2.8mm   |          |           | 0.2m   |  TTL 12,  F.O.V. 140°(D) |
| CA1304A         | ChuangAn    | MP     | Wide     | M8x0.35  | 1 / 2.7" | 105° | F2.4     | 3.53mm  | 5.26mm   |           |        | 55° *105° *138°  10*L9.97mm 5G TTL 14 |
| CA1308C         | ChuangAn    | MP     | Wide     | M8x0.5   | 1 / 4"   | 115° | F2.4     | 2mm     | 4.10mm   |           |        | 87° *115° *170°  12*L10.57mm |
| CA1300I         | ChuangAn    |        | Wide     | M7*P0.35 | 1 / 2.5" | 115° | F2.4     | 2.92mm  | 5.26mm   |           | 0.1m   | TTL:13.97mm, 71° *115° *145°, 10*L10.33mm, 5G+IR  |
| FS2328B13M8     | Focusafe    | MP     | Wide     | M8*0.5   | 1 / 3"   | 115° | F2.8     | 2.3mm   | 5.09mm   |           |        | Flange back 4.5mm, max image circle 6.4mm |
| HK-8244-1042-1  | Guangtongd. | MP     | Wide     | M12*P0.5 | 1 / 2.7" | 120° | F1.8     | 3.0mm   | 6.04mm   |           |        | Flange back 5.2mm, 6G+IR |
| HK-8189-823-1   | Guangtongd. | MP     | Wide     | M12*P0.5 | 1 / 2.7" | 114° | F2.0     | 3.0mm   | 5.98mm   |           |        | Flange back 5.08mm, 6G+IR |
| JSD2157         | JSD         | 5 MP   | Wide     | M12x0.5  | 1 / 2.7" | 148° | F2.0     | 2.35mm  | 4.54mm   |           |        | 6G, TTL 22mm, Lens diameter 17mm |
| JSD1529-A1      | JSD         | MP     | Wide     | M7*P0.35 | 1 / 2.7" | 124° | F2.0     | 2.8mm   | 2.61mm   |           |        | Diameter 10mm, TTL 11.51mm |
| TS-2314T-A10    | TeSoo       | MP     | Fishey   | M7*P0.35 | 1 / 2.3" | 200° | F2.0     | 1.8mm   |          |           |        | Diameter 10mm, TTL 14mm |
| CW-BL2120-3MP   | CWLENS      | 3MP    | Wide     | M12*P0.5 | 1 / 3"   | 115? | F2.0     | 2.1mm   | 5.3mm?   |           |        | Diameter 14mm, TTL 15.8mm ? |
| CW-BL2818-3MP-C | CWLENS      | 3MP    | Wide     | M12*P0.5 | 1 / 2.7" | 112? | F2.0     | 2.8mm   | 5.7mm?   |           |        | Diameter 14mm, TTL 15.3mm ? |

* https://www.lensprocctv.com/3-68mm-M7-CCTV-Lens-Low-Distortion-OV2710-p.html
* https://chancctv.en.alibaba.com/product/60534477516-804927292/1_4_2mm_Board_Lens_with_DFOV_170_degree_Miniature_M8_Lens.html
* https://www.alibaba.com/product-detail/Element-6G-IR-aluminum-glass-plastic_60857424830.html?spm=a2700.wholesale.0.0.55ba6f04EWTHa0
* https://www.alibaba.com/product-detail/m12-mount-OV2735-hd-wide-angle_62351098002.html?spm=a2756.order-detail-ta-bn-b.0.0.486a2fc23vZisF
* https://www.alibaba.com/product-detail/m7-lens-camera-F2-0-diagonal_60302931327.html?spm=a2700.wholesale.0.0.2edffc19WUBCbz
* https://www.towinlens.com/product/ccl127028pmp
* https://gtd.en.alibaba.com/product/62069107306-807693421/Element_6G_IR_back_focal_length_BFL_5_98mm_lens_for_cars.html
* http://www.cwlens.com/en/pd.jsp?id=152#_pp=0_330_6


Best configs

Focusafe FS2328B13M8   M8*0.5, 1/3", 115°,  hyperfocal distance = 63 cm
JSD JSD2157    M12x0.5, 1/2.7", 148°, hyperfocal distance = 92 cm
CW-BL15620-5MP, M12x0.5, 1/3", 185°, hyperfocal distance = 40 cm
TeSoo TS-2314T-A10, M7*P0.35, 1/2.3", 200°, hyperfocal distance = 54 cm


### Lens holders for prototyping.

I'm looking for lens holders that can be mounted on a camera module with 18mm distance between screw holes.
The holder should be as compact as possible and of sizes M12, M8 and M7. Ideally I would like to have a set of each.
The ideal depth of the holders would be 9mm, meaning the total distance from the PCB/FPC to the edge of the hole.
Please provide a technical drawing for the suggested holders.


### M12 holder

M12-1.56MM-5MP   4.3mm
M12-2.1MM-5MP-B  6.9mm
CCL127028PMP     3.0mm, 4.5mm, TTL 12
HK-8244-1042-1   5.2mm, 6.0mm
HK-8189-823-1    5.08mm
JSD2157          4.54mm, TTL 22

7mm - 16mm holder depth


Tesoo optical Co lens holder M12, [D20H90N2](./lenses/D20H90N2.pdf), depth: 9mm
Focusafe BLH004 lens holder M12, 13mm square, 4mm base height, 18mm screw distance, depth: 13mm
Focusafe BLH027, lens holder M12*P0.5, 15mm square, 6.5mm base height, 18mm screw distance, depth: 12mm
TOWIN lens holder M12*P0.5, 18mm screw hole spacing, depth: 9mm
ChuangAn CA5117A lens holder M12, 15.3mm square, base height 3mm, 18mm screw hole spacing, depth 8.8mm
ChuangAn CA5119A lens holder M12, 13.61mm square, 18mm screw hole spacing, depth 9mm
Guangtongd 135-4B-WZ-LCP lens holder M12, 13mm square, 18mm screw hole spacing, depth 8.5mm

### M8 holder

CA1304A          5.26mm, TTL 13.97mm
CA1308C          4.10mm
FS2328B13M8      4.5mm, 5.09mm, max 12mm  
CA5301A          M8*P0.35, max 7.50, base height 3mm, 10mm square

[CA1308C holder](./OV2735-module/lenses/CA1308C-holder.jpg)

Requested ChuangAn lens holder 10mm depth 10mm x 10mm

Focusafe BLH13072, lens holder M8*P0.5, 12mm square, 3.3mm base height, 18mm screw distance, depth: 7.2mm
ChuangAn CA5301A, lens holder M8*P0.35, 10mm square, 3mm base height, no screws, depth: 7.5 mm
ChuangAn CA5303A, lens holder M8*P0.5, 11.45mm square, 3mm base height, no screws, depth: 7 mm


### M7 holder

JSD1529-A1       2.81mm, 2.61, TTL 11.51mm, max 8.7 mm
CA1300I          3.64mm, max 10mm
TS-2314T-A10     5mm ?

ChuangAn lens holder 7mm depth 10mm x 10mm

JSD HA1313_A115P18-052  18mm screw holes. 13mm squared, internally 11.50 squared, M7*P0.35


## AICO lens holder

Black 6mm height plastic M8 m8x0.5 thread 0.5mm mount board car rear view lens socket holder

https://www.alibaba.com/product-detail/Black-6mm-height-plastic-M8-m8x0_60736454859.html?spm=a2700.galleryofferlist.normal_offer.d_image.383e697d6i8agI


## TOWIN Pinhole lens

CCL127028PMP Pinhole lens 2.8mm 1/2.7″ IR 3MP HD CCTV M12 mount lens for Covert hidden Surveillance

 IMAGE FORMAT	1/2.7″
 FOCAL LENGTH	2.8mm
 F.O.V.	140°(D)
 F.O.V.	108°(H)
 RESOLUTION	3 Megapixel
 APERTURE	F2.4
 MOUNT	M12X0.5
 IRIS	Fixed
 FOCUS	Manual
 ZOOM	Fixed
 TTL	12
 M.O.D.	0.2mTowi


TODO follow up on order via e-mail

## Henan Kingopt Import & Export

M12 18mm hole spacing
Holder for 1/2.5" 1/3" 1/4" 
https://www.alibaba.com/product-detail/PC-glass-fiber-18mm-hole-spacing_1600192965995.html?spm=a2700.galleryofferlist.normal_offer.d_title.3a1d2deb77Rsll




## Lenspro Vicky Hou

https://www.lensprocctv.com/3-68mm-M7-CCTV-Lens-Low-Distortion-OV2710-p.html
MTV-0368BF127M7(2MP)
3.68mm M7 Mount 1/2.7
FoV 97°/86.5°/50.5°
1/2.7" F2.8
Distortion 9%
Φ10x8.6mm



[MTV-0228BF14M7(2MP)](https://www.lensprocctv.com/2-28mm-Super-Wide-Angle-M7-Mount-Lens-For-OV2643-p.html)
2.28mm wide angle M7 Mount Mini Lens for OV2643
FoV 130°*110°*95°
1/4" F2.4
Distortion 50%
Φ10x8.4mm
Have: 10 samples. Base tiny, fits only 1/4" sensor

 

 +86 0591-83533213

 sales@lensprocctv.com

 #6104 15th Floor Section A, Complex Building, Fuzhou Free Trade Zone, Fujian province (Free Trade Pilot Zone)




#### Fuzhou ChuangAn Sandra Zhang

1/4" 2mm Board Lens with DFOV 170 degree Miniature M8 Lens

CA1308C


#### Fuzhou .. Focusafe Optics Kelly Lin

* [Focusafe Shop - pinhole lenses](https://focusafe.en.alibaba.com/productgrouplist-815966623/M12_Mount_Pinhole_Lens.html?spm=a2700.shop_plser.98.8)
* [Focusafe Shop - lens holder](https://focusafe.en.alibaba.com/productgrouplist-816180746/Lens_Holder.html?spm=a2700.shop_plgr.98.11)

Model No.	Description	Format Cover (inch)	Mount	Focus Length(mm)	Aperture	Field of View 	Unit Price(USD) EXW FUZHOU
Below 100PCS	100~1000PCS
 
FS2328B13M8	Megapixel IR Board Lens	1/3"	M8*0.5	2.3	2.8	129° 	5.8	5.3
FS3225B2MPM10	Megapixel IR Board Lens	1/3"	M10*0.5	3.2	2.5	99° 	5.8	5.3

Dear Thepia, Good day! Thanks for your enquiry! I want to introduce two lenses which is suitable for your camera, pls check belowing lens list with attached data sheet: Model No. Description Format Cover (inch) Mount Focus Length(mm) Aperture Field of View Unit Price(USD) EXW FUZHOU Below 100PCS 100~1000PCS FS2328B13M8 Megapixel IR Board Lens 1/3" M8*0.5 2.3 2.8 129° US$5.8 US$5.3 FS3225B2MPM10 Megapixel IR Board Lens 1/3" M10*0.5 3.2 2.5 99° US$5.8 US$5.3 Awaiting for your comments and advice! Wish you good business! Thanks & Best regards, Kelly Lin Sales Manager Fuzhou Focusafe Optoelectronic Technology Co.,Ltd. Add:2F Building A,YiQiang Industrial Park,No.13 Jinzhou North Road,Fuzhou,350002 China. Tel: +86 591 83337525 Fax:+86 591 88263182 Cell:+86 (0) 13665052376 Email:sales@focusafe.com Trademanager: focusafe Skype:focusafe http://www.focusafe.com http://focusafe.en.alibaba.com

Communicating via thepia@pm.me
 


#### Fuzhou ChuangAn Jen Lin

**Top option**

Place of Origin:Fujian, China Brand 
Name:ChuangAn 
Model Number:CA1300I 
Focal Length:2.92mm 
Sensor Area:1/2.5" 
Mount Type:M7*P0.35 
Iris Operation:Fixed Iris 
Relative Aperture:2.4 
Angle of view (V*H*D):71° *115° *145° 
Back Focal Length:5.26mm 
TTL:13.97mm 
Dimension:10*L10.33mm 
Structure:5G+IR



Lens M8 104° wide angle
3.53mm 1/2.7" 3mp F2.4 H FOV 104 degree M8 wide angle lens





## Lens DFoV Sandra Zhang - M8 170 deg

CA1308C $2.85 (bought samples)

Focal Length:2mm 
Sensor Area:1/4" 
Mount Type:M8*P0.5 
Iris Operation:Fixed Iris 
Relative Aperture:2.4 
Angle of view (V*H*D):87° *115° *170° 
Back Focal Length:4.01mm 
TTL:13.06mm 
Dimension:12*L10.57mm 
Place of Origin:CN;FUJ Brand Name:ChuangAn


### [Shenzhen Guangtongdian](https://gtd.en.alibaba.com/?spm=a2700.wholesale.cordpanyb.2.225a27d0QNO1kG)

HK-8244-1042-1
[Element 6G+IR aluminum,glass,plastic look around general lens for aerial photo](https://www.alibaba.com/product-detail/Element-6G-IR-aluminum-glass-plastic_60857424830.html?spm=a2700.wholesale.0.0.55ba6f04EWTHa0)

1/2.7" sensor F/ 1.8 f 3.0 mm

FOCAL LENGTH (EFL)	f       3.0       mm
F/NO (INFINITE)	F/NO    1.8 
BACK FOCAL LENGTH	BFL     6.04    mm
FLANGE BACK LENGTH	FB      5.20   mm
FIELD OF VIEW (DIAGONAL)	D:160°H 120°V 60°
OPTICAL DISTORTION (DIAGONAL)	<-78%
Thread Size	M12*P0.5 
Element	6G+IR
Material	Aluminum,glass,plastic
Feature	F/NO:1.8;f:3.0mm

Hyperfocal distance	0.17 m
Hyperfocal near limit	0.09 m
DoF near limit	0.14 m
DoF far limit	∞
Depth of field	∞
Depth of field in front	0.86 m
Depth of field behind	∞



### Shenzhen Jubaolai Electronics Co., Ltd

Camera Auto Focus F1.8 Lens for 12MP 13MP 1/3.1 inch CMOS sensor

Sensor Size:1/3.1'' cmos sensor
EFL:3.86
FNO:1.8
TV Distortion:<1.5%

Shipping by: HK Post
Get datasheet:Plz contact us
Get lowest price:Plz contact us

Place of Origin:TW
Brand Name:Taiwan

Skype:michella_fang


https://keepintegrity.en.alibaba.com/productgrouplist-804449054-3/CMOS_CCD_Sensor.html?spm=a2700.shop_plgr.41413.43.5c7f388dihVsU0&filterSimilar=true&filter=null


### Alternate bird eyes from ChuangAn

Use dual 235° lenses M12

https://www.alibaba.com/product-detail/1-2-3-12MP-235-Degree_1600118157156.html?spm=a2700.details.0.0.1426217633iDlJ

CA347A
Focal Length:    1.41mm
Sensor Area:    1/2.3"
Angle of View (V*H*D):    235° * 235° * 235°
Mount Type:        M12*P0.5
Relative Aperture:    2.0
Back Focal Length:    2.30mm
TTL:    17.71mm
Dimension:    18.5 *15.98mm
Lens Structure:    8G+IR
Image circle:    4.46mm

Ideation: https://www.yankodesign.com/2021/10/06/canons-insane-new-camera-lens-features-two-side-by-side-fisheye-lenses-for-recording-8k-ar-and-vr-footage/



## cwlens.com Shenzhen Chuangwei Video Co.Ltd.

Source for TREEYE ?

CW-BL15620-5MP