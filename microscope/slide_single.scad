tube_lenght=12.0;
r_in = 1.8;
r_out = 2.5;
cover_size=10;
channel_thick=1.0;
support_thick=2.8;
spx=9.5;//support size x
spy=9.5;//support size y
stt=40.0;//space between tube
module tube(){

	
}
difference(){
	union(){
		//tube
		translate([0.0,0,tube_lenght/2.0]){
			cylinder(h=tube_lenght,r=r_out,center=true,$fn=360);
		}	
				
		//support layer
		translate([0,0,support_thick/2.0])cube([spx,spy,support_thick],center=true);
		
	}
	//tubes
	translate([0.0,0,tube_lenght/2.0]){
		cylinder(h=tube_lenght+2*support_thick,r=r_in,center=true,$fn=360);
	}
	//channel
	translate([0,0,channel_thick/2.0])cube([spx,3.0*r_in,channel_thick],center=true);
	//translate([0.0,0.0,channel_thick/2.0]){
		//cylinder(h=channel_thick,r=2.0*r_in,channel_thick,center=true,$fn=360);
	//}
	//cover slide
	//translate([0,0,channel_thick+(support_thick-channel_thick)/2])cube([cover_size,4*r_in,(support_thick-channel_thick+1)],center=true);
}