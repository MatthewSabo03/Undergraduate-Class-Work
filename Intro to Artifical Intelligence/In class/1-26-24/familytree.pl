% Facts
parent(bob, alice).
parent(alice, sarah).
parent(alice, kyle).

% Rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).