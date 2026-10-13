Op dit moment zijn we nog bezig met dit project. Hier een korte uitleg van de scripts:

1. inladen data:
   Omdat het over enorme bestanden gaat, laden we de data in met een forloop van de
   gegeven Caeli API. De datum is te veranderen in de URL.

2. Orbits met aantal:
   In dit script bekijken we hoeveel bruikbare waarnemingen er zijn per orbit.

3. Plot per orbit:
   In dit script maken per orbit een plot. Dit geeft ons inzicht op de missende
   AOD waarde per orbit. Hiermee kunnen we analyseren wat voor artificele missende
   vormen kunnen maken.

4. Zonnige dagen:
   Dit is een testscript wat nog niet af is. We moeten onbewolkte momenten vinden.
   (Dus geen dagen).

5. Interpoleren:
   In dit script interpoleren we de ERA5 data met de MODIS data m.b.v. xarray.
