FROM python:3.6.3-alpine3.4                                                                                  
ADD main.py .                            
EXPOSE 8000                              
ENTRYPOINT python main.py
