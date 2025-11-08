package main

import "fmt"

func main() {
	var n,m int
	fmt.Scanf("%d %d %d",&n,&m)

	for i:=0;i<n;i++{
		if i<m{
			fmt.Println("OK")
		}else{
			fmt.Println("Too Many Requests")
		}
	}
}