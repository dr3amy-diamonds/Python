# 🐼 Ejercicios Prácticos: Filtrado con `.query()` en Pandas

------------------------------------------------------------------------

## 🟢 Ejercicio 1: El Gerente de TI (Filtro Simple)

### Contexto

El Director de Tecnología (CTO) necesita enviar un correo urgente a todo
su equipo.\
Te pide una lista rápida de todos los empleados que pertenecen al
departamento de Tecnología.

### Datos de Entrada

-   Usar el DataFrame `df` creado previamente.
-   Columna clave: `departamento`.
-   Valor buscado: `'IT'`.

### Tu Misión

-   Usar el método `.query()`.
-   Escribir la condición lógica dentro de las comillas como si fuera
    una frase.
-   Mostrar el resultado.

### 📌 Pista lógica

La condición es una igualdad simple:\
`departamento == "IT"`

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Cazatalentos (Lógica AND)

### Contexto

Recursos Humanos está buscando un líder técnico para un nuevo proyecto
crítico.\
El candidato ideal debe cumplir dos requisitos obligatorios:

-   Pertenecer al departamento de `'IT'`.
-   Tener más de 4 años de experiencia.

### Datos de Entrada

-   Usar el DataFrame `df`.
-   Columnas claves: `departamento` y `años_exp`.

### Tu Misión

-   Escribir una sentencia `.query()` que combine ambas condiciones.
-   Usar el operador lógico en inglés `and` en lugar del símbolo `&`.
-   Verificar que solo aparezcan los candidatos senior de IT.

### 📌 Resultado esperado

Deberían aparecer:\
- Luis\
- Marta

------------------------------------------------------------------------

## 🟠 Ejercicio 3: Auditoría de Anomalías (Lógica OR)

### Contexto

El auditor financiero está buscando posibles errores o casos extremos en
la nómina.\
Quiere ver los registros que cumplan cualquiera de estas dos
condiciones:

-   Ganar más de 7000 dólares (salarios altos).
-   Tener menos de 2 años de experiencia (juniors muy nuevos).

### Datos de Entrada

-   Usar el DataFrame `df`.
-   Columnas claves: `salario` y `años_exp`.

### Tu Misión

-   Usar `.query()` para filtrar estas "anomalías".
-   Utilizar el operador lógico `or` para unir las condiciones.
-   Observar cómo `.query()` maneja la precedencia sin necesidad de
    llenar todo de paréntesis.

### 📌 Pista lógica

`salario > 7000 or años_exp < 2`

------------------------------------------------------------------------

## 🔴 Ejercicio 4: El Presupuesto Dinámico (Variables con @)

### Contexto

El presupuesto para bonos cambia cada mes.\
No quieres estar reescribiendo tu código de filtrado cada vez que el
jefe cambia el número.

Hoy, el jefe decidió que el bono es para quienes ganen menos de 6000.

### Datos de Entrada

-   Una variable de Python externa: `limite_bono = 6000`.
-   El DataFrame `df`.

### Tu Misión

-   Definir la variable `limite_bono` en una línea separada antes del
    filtro.
-   Escribir un `.query()` que busque salarios menores (`<`) a esa
    variable.
-   Usar el símbolo `@` para referenciar la variable externa dentro del
    string del `query`.

### 📌 ¿Por qué hacer esto?

Si mañana el límite cambia a 5000, solo cambias la variable, no el
código del filtro.

------------------------------------------------------------------------

## 🟣 Ejercicio 5: La Fiesta de Fin de Año (Listas e `in`)

### Contexto

La empresa hará una fiesta, pero por capacidad del salón solo pueden
invitar a los departamentos administrativos y comerciales.

Debes filtrar a los empleados que trabajen en: - `'Ventas'` - `'HR'`

### Datos de Entrada

-   Una lista de Python: `lista_invitados = ['Ventas', 'HR']`.
-   El DataFrame `df`.

### Tu Misión

-   Definir la lista `lista_invitados`.
-   Usar `.query()` para filtrar el departamento.
-   Utilizar el operador `in` junto con la referencia `@` para conectar
    la lista.

### 📌 Pista lógica

`departamento in @lista_invitados`

------------------------------------------------------------------------

# 🎯 Objetivo General

Al finalizar estos ejercicios, notarás que el código con `.query()` se
lee casi como inglés natural.

Ejemplo conceptual:

`query('salario > @presupuesto and departamento == "IT"')`

Esa es la elegancia y claridad que buscamos al trabajar con Pandas.
