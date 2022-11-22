package main
import(	"os"
	"fmt"
	"flag"
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
)
var db *sql.DB

func main(){
	user	:= flag.String("user", "root", "username");
	pass	:= flag.String("pass", "1234", "password");
	addr	:= flag.String("addr", "127.0.0.1", "ip or dnsname of server");
	port	:= flag.String("port", "3306", "port of sql server");
	dbos	:= flag.String("db", "test", "name on database on server");
	gid	:= flag.String("id", "53", "groupid")
	flag.Parse();
	var err error
	var connstr string = *user + ":" + *pass + "@tcp(" + *addr + ":" + *port + ")/" + *dbos;
	db, err = sql.Open("mysql", connstr);
	errorHandler(err, "can't log to sql");
		
	pingErr := db.Ping()
	errorHandler(pingErr, "server not responding");

	fmt.Println("Succ");

	fmt.Println("X,Y,Z");
	rows, err := db.Query("SELECT * FROM rawdata WHERE groupid = ?", *gid);
	errorHandler(err, "sql querry problems");
	for rows.Next() {
		var X, Y, Z, T string;
		err := rows.Scan(&T, &T, &T, &T, &T, &X, &Y, &Z, &T, &T, &T);
		errorHandler(err, "parsing rows");
		fmt.Printf("%s,%s,%s\n", X, Y, Z);
	}
}

func errorHandler(err error, selite string){
	if err != nil {
		fmt.Println(selite, "\n\t", err);
		os.Exit(2);
	}
}