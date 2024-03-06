# RewardsRadar

### Retrieve up to date cash back categories and percentages for Chase credit cards and insert data into AWS RDS DB.
![image](https://github.com/aww2539/RewardsRadar/assets/52324276/e0c167ec-ec38-4c7b-975a-657e452ea2d7)

### To run:

#### Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)
```bash
pip install pipenv
```

#### Activate shell
```bash
pipenv shell
```

#### Install dependencies from Pipfile
```bash
pipenv install
```

#### Change environment variables to your credentials and RDS DB info
Create a `.env` file from `.env.example` and alter variables accordingly.

#### Run scrape script
```bash
pipenv run scrape
```

