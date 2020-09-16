# Mr. Threat

Mr. Threat is a Django Web-App that allows SOC Analysts to
look up the IPs they're interested in and speed up their workload.
This is an educational project. 

# Live Version

To see an online version go to:

[mr-threat.herokuapp.com](https://mr-threat.herokuapp.com/)

## Usage


1. Check if the IP is malicious. The findings are stored in database.
2. Compare the findings with the most well-known threat-hunting services.
3. First 3 look ups are free then the paid account is needed.

## Tech Stack
 * Python Django 3.0
 * PostgreSQL
 * HTML, CSS, Bootstrap

## Instalation

1. Create virtual env.
2. pip install requirements.txt
3. Remember to set up a secret key and APIs keys
4. Migrate the database.
5. Run: python manage.py runserver
6. Go to local host.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)