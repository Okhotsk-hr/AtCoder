package main

import "fmt"

func main() {
	var s,a,b,x int
	var run int
	run=0
	fmt.Scanf("%d %d %d %d",&s,&a,&b,&x)

	for x>0{
		if x>=a{
			run+=s*a
			x-=a+b
		}else{
			run+=s*x
			x=0
		}
	}

	fmt.Println(run)
}