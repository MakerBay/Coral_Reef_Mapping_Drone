# Coral Reef Mapping Drone
## An open source ocean water drone used for mapping and analyzing the health of coral reefs

# What we're doing ? 
We are Designing a Coral Reef Mapping Drone

# But, what exactly is this? 
Basically, we want to design and fabricate an ocean robot, think remote control boat but that has high quality cameras for capturing what's under the surface and then the ability to set it to autonomous cruise mode and our sailing robot will return after 3 hours with lots of images of coral reefs for scientists to analyse. Whats more is that our robot will be able to analyse the coral itself with onboard A.I features. 

# Why are we doing this? 

Coral reefs are essential to healthy coasts and vibrant economies, playing a critical role in everything from protecting lives and property to supporting thousands of businesses.
Climate change is the biggest threat to the world’s coral reefs, causing mass bleaching, among other things. 

Office for Coastal Management, National Oceanic and Atmospheric Administration

https://coast.noaa.gov/states/fast-facts/coral-reefs.html

! [Coral Reef date image from NOA] (https://drive.google.com/drive/folders/1pXe8e5yRKJEjRXpZvbHnNLRLgVJu99Ym)



The third global bleaching event, from 2014 to 2017, brought mass bleaching-level heat stress to more than 75 percent of global reefs; nearly 30 percent also suffered mortality level stress. This bleaching event was the longest, most widespread, and most destructive on record. 

https://www.ametsoc.net/sotc2017/StateoftheClimate2017_lowres.pdf

“There are efforts to use drones or satellites to collect this information, but you cannot get the high resolution needed to assess the vital complex architecture of reefs unless you are in the water,” 
Joleah Lamb 
World Economic Forum

https://www.weforum.org/agenda/2019/08/what-a-million-corals-in-2-500-reefs-tell-us-about-saving-them




Our innovations:
* #1 Diver -> Ocean Surface Drone
* #2 Mechanical Quadrat -> Laser quadrat
* #3 Manual mapping -> Integrated workflow from imaging, map, to data

Our goal is to make coral reef mapping
- 10x faster
- 10x more accurate
- 10x cheaper than state of the art

![Photo of Mustard seed](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550258199216-EWPQCILYKOOI7MGPXO5F/ke17ZwdGBToddI8pDm48kBZw6jF4_OvU-ddo_vwqGhp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Ub61YCrK70I7JIpWiI8ho4Yi1WvVNQtDE81xuRbL1MFKm0sD-Bab7E9MY8W31A7zMQ/33230060508_aa5fc9a347_k.jpg?format=1500w)

![Photo of 3d coral mapping](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1530466231826-FNW4LDAH7XH30ZFNJJAH/ke17ZwdGBToddI8pDm48kLm-eDV0ETPZElAUOuRm5LoUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYy7Mythp_T-mtop-vrsUOmeInPi9iDjx9w8K4ZfjXt2dozICiKierPdirwma1lhz985X3tnvptEZXlQK7_WXsWuOpYghpI-Ha_TwZsqqmJXng/25114424537_f4074ea83e_o.jpg?format=2500w)

[18.0 Scoutbot Mustard](https://www.scoutbots.com/protei#/18-scoutbot-mustard/) is a semi-autonomous boat that is targeted to map coral reefs. It has both remote control (RC) capacity as well as route planning using the Pixhawk microcontroller. This prototype has back function and can rotate on itself: it is highly maneuverable and can navigate in narrow and shallow areas

### Specifications

 * **Footprint:** 1.2m x 1.0m x 0.4m
 * **Weight:** <8kg
 * **Speed:** 0.5m/s for Auto mission (2.0m/s max)
 * **Runtime:** 4S (14.8V) 10000mAH
 * **1 hour Coverage:** = 7000m2/hour; ~340 pictures (assuming 5m depth water)
 * **Image Resolution:** 0.3 - 2cm/pixel (GoPro). Can upgrade better camera or multi-spectral, Can carry a camera Canon 5d mark 4 with a sea & sea underwater housing (60m)
 * **Depth of observation:** Observe from 0.5m to 10m depending on visibility
 * **Control/Telemetry Range:** 2km (Recommend to add a front facing real time image transmission system if moving beyond line of sight),  * Manual Override, Auto Return Home
 * **Optional Features:** Environmental Sensors, Real time telemetry sync to cloud
 * **Hardware Cost:** <1000 USD
 * **Time to build:** 4 days 
 
This version was built by the [Scoutbots team](https://www.scoutbots.com/) Ken Chew, Eddie Yung, [Cesar Jung-Harada](https://cesarjungharada.com/) and Sameer Kunde

![photo of ken and eddie](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550258135664-IRNOSGZWSGIQVUW2TRS3/ke17ZwdGBToddI8pDm48kBZw6jF4_OvU-ddo_vwqGhp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Ub61YCrK70I7JIpWiI8ho4Yi1WvVNQtDE81xuRbL1MFKm0sD-Bab7E9MY8W31A7zMQ/46178780194_3433a0177d_k.jpg?format=1500w)

Eddie Yung and Ken Chew

![Photo of Cesar and eddie](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550258245745-T0HT4CPK5MZOU86S1A2U/ke17ZwdGBToddI8pDm48kPK79jU1XeGeFdNPGu_Z9LF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QHyNOqBUUEtDDsRWrJLTmNFveLtSPA03JKuAUT-dZqxKOlW1dmcyva0SWFCfnfPCLzLhnXQa_AnJz627O8vAp/45989089115_abc0642138_o.jpg?format=1500w) 

Eddie Yung and [Cesar Jung-Harada](https://cesarjungharada.com/)

![Photo of PMQ exhibit](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550258114745-6H322KIJ8UBDTTE7USVS/ke17ZwdGBToddI8pDm48kNKt-pHDXrzwAjIfSk5SYbN7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UcnvRtzEwdgNk4gmcis-V6EWlYXsfTfPGXQTK5kyyTmWVui_uwT1L0qH0SjV2jNRDA/46251813322_49a14e8090_o.jpg?format=1500w)

Thanks to Kamakshi Ajoy Bhavnani for the coral reef artwork and Thomas Williams for the exhibit stage

![photo of camera on boat](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550258175244-3BWT20Q0EC5LP2VEWLNN/ke17ZwdGBToddI8pDm48kBZw6jF4_OvU-ddo_vwqGhp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Ub61YCrK70I7JIpWiI8ho4Yi1WvVNQtDE81xuRbL1MFKm0sD-Bab7E9MY8W31A7zMQ/39938969743_ed255bea6f_k.jpg?format=1500w)

![photo of mustard in the water](https://images.squarespace-cdn.com/content/v1/588c5e468419c2ec3fced0c0/1550257296501-II5UUJ2HHY6U9GGWNO5A/ke17ZwdGBToddI8pDm48kBZw6jF4_OvU-ddo_vwqGhp7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Ub61YCrK70I7JIpWiI8ho4Yi1WvVNQtDE81xuRbL1MFKm0sD-Bab7E9MY8W31A7zMQ/46178779444_b65c54a0cc_k.jpg?format=1500w)

# Sub Teams
## Hardware / Mechanical, 3D printing
Michael, Paul, Ming, Brad, Abbas 

## Electric, Electronics
Jacques, Cesar, Matthew, Alvaro 

## IT, Software, UX/UI
Adel, Matthew, Celine, Philippe

## AI, Biology 
Sanjeew, Maxine, Kamakshi, Nicholas
