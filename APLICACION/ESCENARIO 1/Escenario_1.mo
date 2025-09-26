model Escenario_1
  // Variable de estado
  Real h(start=14);   // Altura inicial de 14 m
equation
  der(h) = -0.25;     // dh/dt = -0.25 m/día

end Escenario_1;
