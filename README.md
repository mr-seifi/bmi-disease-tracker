# Disease Tracker

## Models

### Person
- __email__: string
- __password__: string
- __age__: integer
- __sex__: string (male, female)
- __weight__: float
- __height__: float

> Person is a model which inherited from django.contrib.auth.User hence we can define authentication for each instance 
> of this class. also each person has some feature like weight and height which can help us with calculating BMI.

### InTimeBio
- __person__: integer
- __country__: string
- __smoker__: boolean
- __hip__: float
- __waist__: float
- __wrist__: float
- __neck__: float
- __current_heart_rate__: float
- __daily_activity_level__: string (low, medium, high)
- __blood_pressure_sys__: float
- __blood_pressure_dia__: float

> InTime company has some feature from each person that I mentioned above, we provide so many recommendations 
> and risks when we have a good mapping between these features and recomms/risks.

### BloodTest
- __person__: integer
- __urea__: float
- __cr__: integer
- __hba1c__: float
- __chol__: float
- __tg__: float
- __hdl__: float
- __ldl__: float
- __vldl__: float
- __result__: string (Y, N, P)
> Blood Test model defines a blood test of a person based on the results of that and some parameters which are measured
> in that test therefore you can see urea, cr (creatinine), hba1c, and so many fields. each instance belong to a person.

### Recommendation
- __blood_type__: string (Y, N, P)
- __recommendation__: string
> Some recommendations which classified by the result of blood test. so you can filter blood_type=Y 
> if you get Y in your blood test to see a bulk of recommendations.


## API

### Swagger
- endpoint: `/`

### Signup
- endpoint: `account/signup/`
- method: `POST`
- params: `email, password*, age*, sex*, weight*, height*`
- permissions: `AllowAny`
> You can sign up as a person in our system by providing above parameters after that you are given a token which 
> is used to have some tests like blood test and see the result of your test (recomms/risks)

### Submit a Blood Test
- endpoint: `bio/bloodtest/`
- method: `POST`
- params: `urea*, cr*, hba1c*, chol*, tg*, hdl*, ldl*, vldl*`
- permissions: `IsAuthenticated`
> To submit a blood test you have to sign up first, after that, put your token into your header of requests like this: 
> `Authorization: Token <token>` hence system identifies you as a valid user.

### Get result of your Blood Tests (Recommendations/Risks)
- endpoint: `bio/bloodtest/`
- method: `GET`
- params:
- permissions: `IsAuthenticated`
> By calling this endpoint, you can have a list of blood test result.


## Run Project

### Run Server
```shell
python manage.py runserver
```

### Run beat
```shell
celery -A bmi_disease_tracker beat -l info
```

### Run worker
```shell
celery -A bmi_disease_tracker worker -l info
```