BEGIN{
        FS=","
}
{
gsub("'","''")
id=$1
country=$3
began=$4
ended=$5
days=$6
deaths=$7
displaced=$8
damage_usd=$9
main_cause=$10
severity=$11
sq_km=$12
magnitude=$13
x=$14
y=$15
}
id !~ /register/ {
        printf "INSERT INTO effects VALUES ("magnitude","severity","deaths","displaced","damage_usd",'"cause"',"id");\n" ;
        printf "INSERT INTO locations VALUES ( '("x","y")'::POINT, "sq_km", '"country"',"id");\n"
        printf "INSERT INTO dates VALUES ( '"began"','"ended"',"days","id");\n"
}
