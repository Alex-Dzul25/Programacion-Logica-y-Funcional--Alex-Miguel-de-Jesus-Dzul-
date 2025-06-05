% ----- Datos de entrada por lugar -----
% lugar(Nombre, Humedad, Temperatura, Hora, PronosticoLluvia).
lugar(huerto, baja, 35, 20, false).
lugar(jardin, media, 28, 9, true).
lugar(vivero, baja, 33, 7, false).
lugar(patio, alta, 30, 21, false).

% ----- Reglas generales -----

% 1. Una hora es adecuada si es antes de las 10 am o después de las 6 pm
hora_adecuada(Hora) :- Hora < 10 ; Hora > 18.

% 2. Activar riego si se cumplen condiciones en ese lugar
activar_riego(Lugar) :-
    lugar(Lugar, baja, _, Hora, false),
    hora_adecuada(Hora).

% 3. Estado del riego por lugar
estado_riego(Lugar, 'Activado') :- activar_riego(Lugar), !.
estado_riego(Lugar, 'No Activado') :- \+activar_riego(Lugar).

% 4. Alerta por temperatura elevada
alerta_calor(Temp) :- Temp >= 32.

% 5. Recomendaciones específicas por lugar
recomendacion(Lugar) :-
    lugar(Lugar, _, Temp, Hora, _),
    activar_riego(Lugar),
    alerta_calor(Temp),
    Hora > 18, !,
    format('Lugar: ~w~nAlerta: Riego activado con temperatura alta en horario nocturno.~nRecomendación: Usar sistema por goteo o intervalos cortos.~n~n', [Lugar]).

recomendacion(Lugar) :-
    lugar(Lugar, _, Temp, _, _),
    activar_riego(Lugar),
    alerta_calor(Temp), !,
    format('Lugar: ~w~nAlerta: Riego activado con temperatura alta.~nRecomendación: Evite evaporación; use métodos eficientes de riego.~n~n', [Lugar]).

recomendacion(Lugar) :-
    activar_riego(Lugar), !,
    format('Lugar: ~w~nRiego activado. Condiciones normales.~nRecomendación: Mantener supervisión periódica.~n~n', [Lugar]).

recomendacion(Lugar) :-
    \+activar_riego(Lugar),
    format('Lugar: ~w~nRiego no activado. No se requieren acciones.~n~n', [Lugar]).
