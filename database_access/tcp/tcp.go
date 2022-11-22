package main

import (
	"io"
	"fmt"
	"net"
	"flag"
	"bytes"
	"strings"
	"encoding/csv"
)

func main() {
	//commanline flags
	groupid := flag.String("id", "53", "groupid");
	flag.Parse();

	//connect to server
	fmt.Printf("conn\n")
	con, err := net.Dial("tcp", "172.20.241.9:20000")
	if err != nil{
		con.Close()
		return
	}

	//send the command to server
	msg := *groupid+"\n"
	_, err = con.Write([]byte(msg))
	fmt.Println(err)
	if err != nil{
		con.Close()
		return
	}

	//read data from server
	var buf bytes.Buffer
    	io.Copy(&buf, con)

	//process to csv
	r := csv.NewReader(strings.NewReader(buf.String()))
	r.Comma = ' ';
	records, err := r.ReadAll();
	fmt.Println("X,Y,Z");
	for _, record := range records {
		if len(record) == 11{
			fmt.Printf("%s,%s,%s\n", record[5], record[6], record[7]);
		}
	}

	con.Close()
}