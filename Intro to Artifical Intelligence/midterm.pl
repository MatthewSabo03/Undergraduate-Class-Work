owns(brian, car(mazda)).
owns(chad, car(mazda)).
owns(majid, car(mercedes)).
owns(rachel, car(ford)).

hatchback(car(mazda)).
sedan(car(sedan)).
truck(car(ford)).

drives_manual(X) :- owns(X, _), hatchback(_).
drives_manual(X) :- owns(X, _), truck(_).
