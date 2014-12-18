pcbz=3.55;
r1=13.45;
r2=15.00;
h1=3.5;
h2=20;
shell=3;
module tube(){
	difference(){
		union(){
			translate([0,0,-(h1+h2)])cylinder(h=h1+h2,r=r2+shell,$fn=360);
			translate([0,0,-0.5*h1])cube([2*(r2+2*shell),2*(r2+2*shell),h1],center=true);
			translate([0,0,0.5*pcbz])cube([2*(r2+2*shell),2*(r2+2*shell),pcbz],center=true);
		}
		translate([0,0,-h1])cylinder(h=h1,r=r1,$fn=360);
		translate([0,0,-(h1+h2)])cylinder(h=h2,r=r2,$fn=360);
	}
}
module picam(){
	se=10.5;//sunny edge
	pcbx=25.0;
	pcby=24.0;
	
	camxy=8.0;
	camz=4.5;	
	//pcb
	translate([-pcbx/2,-se-camxy/2,0]) cube([pcbx,pcby,pcbz]);
	//cam
	translate([-camxy/2,-camxy/2,-camz])cube([camxy,camxy,camz]);
	//sunny
	translate([-camxy/2,-se-camxy/2,-2])cube([camxy,se,2.0]);
	//cable
	translate([(-16)/2,pcby-se-camxy/2,2])cube([16,100,0.25]);
}
module cover(){
	tm=1.3; //thickness of the cable cover pad
	translate([0,0,1.5*pcbz])cube([2*(r2+3*shell),2*(r2+2*shell),pcbz],center=true);
	//translate([(-16)/2,pcby-se-camxy/2, 1.5*pcbz-tm])cube([16,(r2+2*shell),tm]);
	translate([-8,0, 1*pcbz-tm])cube([16,(r2+2*shell),tm]);
	translate([r2+2*shell,0.0,0.5*pcbz])cube([2*shell,2*(r2+2*shell),pcbz],center=true);
	translate([-(r2+2*shell),0.0,0.5*pcbz])cube([2*shell,2*(r2+2*shell),pcbz],center=true);
	translate([r2+2*shell,0.0,-0.5*h1])cube([2*shell,2*(r2+2*shell),h1],center=true);
	translate([-(r2+2*shell),0.0,-0.5*h1])cube([2*shell,2*(r2+2*shell),h1],center=true);
}
module platform(){	
	h=56;//x
	w=85;//y
	r=3.5;//round radius
	hr=1.4;	
	hh=49;//x
	hw=58;//y
 	yshift=-1;
	difference(){
		roundrect(h,w,r);
		//translate([-(h-r)/2,+(w-r)/2])cylinder(h=shell,r=hr,$fn=360);
		//translate([+(h-r)/2,+(w-r)/2])cylinder(h=shell,r=hr,$fn=360);
		//translate([-(h-r)/2,+(w-r)/2-58])cylinder(h=shell,r=hr,$fn=360);
		//translate([+(h-r)/2,+(w-r)/2-58])cylinder(h=shell,r=hr,$fn=360);
		translate([-hh/2,yshift+(w-r)/2,0])cylinder(h=shell,r=hr,$fn=360);
		translate([+hh/2,yshift+(w-r)/2,0])cylinder(h=shell,r=hr,$fn=360);
		translate([-hh/2,yshift+(w-r)/2-58,0])cylinder(h=shell,r=hr,$fn=360);
		translate([+hh/2,yshift+(w-r)/2-58,0])cylinder(h=shell,r=hr,$fn=360);
	}	
} 

module roundrect(h,w,r){
	translate([-(h-r)/2,-(w-r)/2,0])cylinder(h=shell,r=r,$fn=360);
	translate([-(h-r)/2,+(w-r)/2,0])cylinder(h=shell,r=r,$fn=360);
	translate([+(h-r)/2,-(w-r)/2,0])cylinder(h=shell,r=r,$fn=360);
	translate([+(h-r)/2,+(w-r)/2,0])cylinder(h=shell,r=r,$fn=360);
	translate([0,0,shell/2.0])cube([h+r,w-r,shell],center=true);
	translate([0,0,shell/2.0])cube([h-r,w+r,shell],center=true);
}

//cover
union(){
	translate([0,-11,7])platform();
	difference(){
		cover();
		picam();
	}
} 

//tube
translate([0,0,-20]){
	difference(){
		tube();
		cover();
		picam();
	}
}
