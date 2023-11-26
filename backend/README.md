
#### Install libraries
```cmd
pip install fastapi
pip install "uvicorn[standard]"
```

#### Run
```cmd
python -m uvicorn main:app --reload
```


## Pydantic Model Setting

### [Field](https://docs.pydantic.dev/latest/concepts/fields/)

#### Numeric Constraints
* `gt`: greater than
* `lt`: less than
* `ge`: greater than or equal to
* `le`: less than or equal to
* `multiple_of`: a multiple of the given number
* `allow_inf_nan1`: allow 'inf', '-inf', 'nan' value

#### String Constraints
* `min_length`: Minimum length of the string.
* `max_length`: Maximum length of the string.
* `pattern`: A regular expression that the string must match.


#### Decimal Constraints
* `max_digits`: Maximum number of digits within the Decimal. It does not include a zero before the decimal point or trailing decimal zeroes.
* `decimal_places`: Maximum number of decimal places allowed. It does not include trailing decimal zeroes.