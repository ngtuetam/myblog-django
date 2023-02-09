FROM python:3.8.3-alpine


# install dependencies
RUN apk update && apk upgrade
RUN apk add --no-cache gcc \
                       libc-dev \
                       libffi-dev
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy source-codes
COPY myblog/myblog/ /app/myblog/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]