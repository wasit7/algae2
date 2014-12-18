r1=13.45;
r2=15.00;
h1=3.5;
h2=30;
shell=3;
module tube(h1,h2,r1,r2){
	difference(){
		cylinder(h=h1+h2,r=r2+shell,$fn=360);	
		translate([0,0,-1])cylinder(h=h1+h2+2,r=r1,$fn=360);
		translate([0,0,-1])cylinder(h=h2+1,r=r2,$fn=360);
	}
}
module picam(){
	se=10.5;//sunny edge
	pcbx=25.0;
	pcby=24.0;
	pcbz=3.55;
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
module comb1(){
	cx=40;
	cy=40;
	cz=5;
	dshell=0;
	dx=cx+2*dshell;
	dy=cy+2*dshell;
	dz=cz+2*dshell;
	//case c
	translate([-cx/2,-cy/2,h1+h2])cube([cx,cy,cz]);
	//case d
	//translate([-dx/2,-dy/2,h1+h2-dshell])cube([dx,dy,dz]);
	
	tube(h1,h2,r1,r2);
}
module cover(){
	cx=40;
	cy=40;
	cz=5.1;
	ez=1.5;
	fz=1.4;
	translate([-cx/2,-cy/2,h1+h2+cz])cube([cx,cy+5,ez]);
	bx=16;
	by=10.6;
	bz=1.5;
	translate([-bx/2,cy/2-by,h1+h2+cz-fz])cube([bx,by+5,fz]);
}
//cover();
//translate([0,0,h1+h2+1.5]) picam();
//comb1();

difference(){
	comb1();
	cover();		
	translate([0,0,h1+h2+1.5]) picam();
}

