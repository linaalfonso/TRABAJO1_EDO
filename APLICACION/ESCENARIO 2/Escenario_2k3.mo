model Escenario_2k3
  parameter Real h0 = 14; // m
  parameter Real k = 1; // m^2/día 
  parameter Real w = 20;
  parameter Real z = 20;
  Real h(start=h0);
equation
  der(h) = - (k/(w*z)) * h; // dh/dt (unidad m/día)
end Escenario_2k3;
