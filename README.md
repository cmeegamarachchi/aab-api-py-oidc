# aaf-api-py
appsolve application blocks fast-api starter kit  

`aab-api-py-oicc` is a Python, Fast-API based api starter kit with open-id-connect authentication. Its build around best practices such as router based feature moudles.  

Some of the highlevel features  
1. Feature modules. All features are hosted in `features` folder and common code is hosted in `common` folder

### To start

Add required environment. `.env` at root level is supported. Following environment variables are required  
  * `OIDC_APP_CLIENT_ID`: App client id
  * `OIDC_JWKS_URL`: JWT keys url
    * For Azure: `https://login.microsoftonline.com/[TENENT_ID]/discovery/v2.0/keys`
    * For cognito: `https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USERPOOL_ID}/.well-known/jwks.json`
  * `OIDC_ISSUER`:
    * For Azure: `https://login.microsoftonline.com/ae5a8cb0-673c-43ba-826c-c2d6c87f2d70/v2.0`
    * For cognito: `https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USERPOOL_ID}` 

Install the dependencies and execute 
```bash
cd api
pip install -r requirements.txt
cd ..
uvicorn api:app --reload
```