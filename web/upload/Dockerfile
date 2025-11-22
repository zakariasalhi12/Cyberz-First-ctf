FROM php:8.2-apache

# Change Apache internal port to 8822
RUN sed -i 's/80/8822/g' /etc/apache2/ports.conf && \
    sed -i 's/:80/:8822/g' /etc/apache2/sites-available/000-default.conf

# Copy challenge files
COPY . /var/www/html/

# Permissions for uploads
RUN chmod -R 777 /var/www/html/uploads

EXPOSE 8822

CMD ["apache2-foreground"]
