% Datos de entrada
humedad_suelo(baja).
temperatura(35).
hora(20).
pronostico_lluvia(false).

% Reglas

% 1. La hora adecuada para regar es antes de las 10:00 a. m. o después de las 6 p. m.
hora_adecuada :- hora(H), (H < 10 ; H > 18).

% 2. El riego se activa automáticamente si:
% -- La humedad del suelo es baja
% -- No se pronostica lluvia
% -- Es una hora adecuada para regar
activar_riego :- humedad_suelo(baja), pronostico_lluvia(false), hora_adecuada.

% 3. Estado del riego: Activado si se cumple la condición, No activado en caso contrario.
estado_riego('Activado') :- activar_riego.
estado_riego('No Activado') :- \+activar_riego.

% 4. Alerta por condiciones externas:
% Si la temperatura es mayor o igual a 32 °C, se activa una alerta por calor extremo.
alerta_calor :- temperatura(T), T >= 32.

% Si el riego se activa bajo esas condiciones, el sistema emite una recomendación.
recomendacion :-
    activar_riego,
    alerta_calor, !,
    writeln('Alerta: riego activado con temperatura alta.'),
    writeln('Considere riego nocturno o por goteo').

% Si no hay condiciones especiales, no hay recomendaciones.
recomendacion :- writeln('Sin recomendaciones').
