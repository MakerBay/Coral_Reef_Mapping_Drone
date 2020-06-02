
# Lua Script for ardupilot
https://ardupilot.org/copter/docs/common-lua-scripts.html


# Codes that are being used

## Location
Location() - Allocate an empty location object
lat( [new_lat] ) - If there's no argument, returns curretn latitude in degree as integer. If there's one argument, it will assign value to the latitude

lng( [new_lng] ) - If there's no argument, return current longitude in degree as integer. If there's one argument, it will assign value to the longtitude

relative_alt( [is_relative]) - If returns as true, location is planned as relative to home. If return as boolean value(T/F) then it will set relative altitude

origin_alt( [is_origin] ) - If returns true, location is planned in absolute altitude relative to mean sea level. If return boolean value(T/F) then it  will set the altitude to be relative to mean sea level.

get_distance( other_Location ) - Calculates horizontal distance between two locations in metres

offset( offset_north, offset_east ) - translates this location by specified numbers of metres




## Vector2f

### compnets stored as floating point numbers

Vector2f() - allocate a new vector2f

x( [new_x] ) - If no argument then it will return current SetX component as floating number. If there's one argument, it will assign value to X component

y( [new_y] ) - If no argument then it will return current SetY component as floating number. If there's one argument then it will asssign value to Y component

length() - Returns the length of the vector as a floating number 

normalize() - Normalise the vector to be unit vector( vector of length 1)

is_nan() - If return true, vector contains any NaN members( Not A Number)

is_zero() - If returns true, all vector fields=0

is_inf() - if reurns true, vector contains any infinity members

"+" : Adds two vectos by components
"-" : Subtacts two vectors by components



## Vector3f
### holds 3D vectors
### components stored as floating numbers

x( [new_x] ) - If no argument then it will return current SetX component as floating number. If there's one argument, it will assign value to X component

y( [new_y] ) - If no argument then it will return current SetY component as floating number. If there's one argument then it will asssign value to Y component

z( [new_z] ) - If no argument then it will return current SetZ component as floating number. If there's one argument then it will assign value to Z component

length() - Returns the length of the vector as a floating number 

normalize() - Normalise the vector to be unit vector( vector of length 1)

is_nan() - If return true, vector contains any NaN members( Not A Number)

is_zero() - If returns true, all vector fields=0

is_inf() - if reurns true, vector contains any infinity members

"+" : Adds three vectos by components
"-" : Subtacts three vectors by components



## Arming (arming:)
### Provides access to arming status and commands


disarm() - Disarm vehicle in all cases. If it's already disarmed then return as false

is_armed() - If vehicle is currently armed then it will return as true

arm() - Attempts to arm the vehicle. If successful then returns as true



## Battery (battery:)
### Provides access to information ablut currently connected batteries

num_instances() - return nmber of battery instances currently available

healthy( instance ) - If requested battery instance is healthy, it will return true. *Healthy means that ArduPilot able to monitor the battery*

capacity_remaining_pct( instance ) - Returns remaining percentage of battery (0-100)

overpower_detected( instance ) - If too much power is being drawn from the battery being monitored then it will return as true

get_temperature( instance ) - returns the temperature of battery in degrees Celcius



## GPS(gps:)
### Provides access to information about GPS's on the vehicle

num_sensors() - returns number of connected GPS devices. If GPS blending is turned on then it will show up as third sensor

primary_sensor() - return which GPS is currently being used as the primary GPS device

status ( instance ) - returns the GPS fix status

location ( instance ) - returns location userdata for last GPS position. Check the status to know if it's still current, if it is NO_GPS or NO.FIX then it would return as old data

speed_accuracy( instance ) - Return as Nil or return as speed accuracy of the GPS in metre per second

velocity( instance ) - returns as Vector3f contains velocity as obsvered by GPS

get_antenna_offset( instance ) - return as vector3f that contains offsets of GPS in metres in body frame

first_unconfigured_gps() - Returns nil or the instance number of the first GPS that has not been fully configured. If all GPS’s have been configured this returns 255 if all the GPS’s have been configured 




### GCS(gcs:)

send_text( severity, text ) - send text string with message severity level



<img src="https://github.com/MakerBay/Coral_Reef_Mapping_Drone/blob/master/3_Boat%20Software/Severity%20level.JPG" width=200>




## Terrain(terrain:)
### Provides access to check heights of terrain

enabled() - Returns true if terrain is enabled

height_terrain_difference_home (location ) - returns the height between provided location and home in metres. If not availble then it will return as Nil
