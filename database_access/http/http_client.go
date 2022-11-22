package main
import(	"os"
	"fmt"
	"flag"
	"strings"
	"io/ioutil"
	"net/http"
	"encoding/csv"
)

func main(){
	//flags
	groupid := flag.String("id", "53", "groupid");
	flag.Parse();
	
	//get data
	resp, err := http.Get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=" + *groupid);
	errorHandler(err, "can't get data from server");
	body, err := ioutil.ReadAll(resp.Body);
	errorHandler(err, "can't read body");
	//fmt.Println(string(body));
	
	//process to csv
	r := csv.NewReader(strings.NewReader(string(body)))
	r.Comma = ';';
	records, err := r.ReadAll();
	fmt.Println("X,Y,Z");
	for _, record := range records {
		fmt.Printf("%s,%s,%s\n", record[5], record[6], record[7]);
	}
}

func errorHandler(err error, selite string){
	if err != nil {
		fmt.Println(selite, "\n\t", err);
		os.Exit(2);
	}
}