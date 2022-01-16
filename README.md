# CSV to JSON/YAML Converter
As the name suggests, converts a CSV file into JSON and YAML files

#### Sample Input (.csv)

```
id,first_name,last_name,email
1,Alie,Amort,aamort0@github.io
2,Verile,Fayers,vfayers1@indiatimes.com
```

#### Sample Output (.json)

```
{
    "1": {
        "id": "1",
        "first_name": "Alie",
        "last_name": "Amort",
        "email": "aamort0@github.io"
    },
    "2": {
        "id": "2",
        "first_name": "Verile",
        "last_name": "Fayers",
        "email": "vfayers1@indiatimes.com"
    }
}
```

#### Sample Output (.yaml)

```
id : 1
first_name : Alie
last_name : Amort
email : aamort0@github.io

id : 2
first_name : Verile
last_name : Fayers
email : vfayers1@indiatimes.com
```
