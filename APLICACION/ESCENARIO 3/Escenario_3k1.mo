model Escenario_3k1
  // Parámetros 
  parameter Real H    = 20      "Altura máxima (m)";
  parameter Real w    = 20      "Largo (m)";
  parameter Real z    = 20      "Ancho (m)";
  parameter Real b    = 100     "Caudal base (m^3/día)";
  parameter Real k    = 0.1     "Constante de salida (m^2/día)";
  parameter Real omega = 2*Modelica.Constants.pi/180 "Frecuencia (rad/día)";

  // Estado
  Real h(start = 0.7*H) "Altura inicial = 70% de H (m)";

equation
  // Ecuación 
  der(h) = ( b + b*sin(omega*time) - k*h ) / (w*z);
end Escenario_3k1;
