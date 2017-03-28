select 'a', 
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 01
	   and b.idempresa = 1
	) Janeiro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 01
	   and b.idempresa = 1
	) Janeiro2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 02
	   and b.idempresa = 1
	) Fevereiro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 02
	   and b.idempresa = 1
	) Fevereiro2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 03
	   and b.idempresa = 1
	) Marco2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 03
	   and b.idempresa = 1
	) Marco2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 04
	   and b.idempresa = 1
	) Abril2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 04
	   and b.idempresa = 1
	) Abril2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 05
	   and b.idempresa = 1
	) Maio2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 05
	   and b.idempresa = 1
	) Maio2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 06
	   and b.idempresa = 1
	) Junho2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 06
	   and b.idempresa = 1
	) Junho2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 07
	   and b.idempresa = 1
	) Julho2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 07
	   and b.idempresa = 1
	) Julho2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 08
	   and b.idempresa = 1
	) Agosto2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 08
	   and b.idempresa = 1
	) Agosto2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 09
	   and b.idempresa = 1
	) Setembro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 09
	   and b.idempresa = 1
	) Setembro2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 10
	   and b.idempresa = 1
	) Outubro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 10
	   and b.idempresa = 1
	) Outubro2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 11
	   and b.idempresa = 1
	) Novembro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 11
	   and b.idempresa = 1
	) Novembro2015,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2016
	   and b.mes = 12
	   and b.idempresa = 1
	) Dezembro2016,
	(
	select b.diasuteis
	  from dbContabil.cadparam b
	 where b.ano = 2015
	   and b.mes = 12
	   and b.idempresa = 1
	) Dezembro2015

from dual;
