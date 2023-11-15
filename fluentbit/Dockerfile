# Utiliza una imagen base ligera de Ubuntu Server
FROM ubuntu:20.04

# Actualiza el sistema e instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Configura la clave GPG de Fluent Bit
RUN curl -L https://packages.fluentbit.io/fluentbit.key | gpg --dearmor -o /usr/share/keyrings/fluentbit-keyring.gpg

# Agrega el repositorio de Fluent Bit
RUN echo "deb [signed-by=/usr/share/keyrings/fluentbit-keyring.gpg] https://packages.fluentbit.io/ubuntu/focal focal main" > /etc/apt/sources.list.d/fluentbit.list

RUN curl https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh | sh
# Copia tu archivo de configuración de Fluent Bit al contenedor
COPY fluent-bit.conf ./fluent-bit.conf
COPY parser.conf ./parser.conf
COPY nginx.logs ./nginx.logs

# Ejecuta Fluent Bit
CMD tail -f /dev/null
