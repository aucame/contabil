
SELECT a.codigo, 
       a.descricao,
       (select b.valor 
          from dbContabil.cadlancamento b
		 where b.ano = 2015
           and b.mes = 01
           and b.idplano = a.codigo
       ) Janeiro2015,
       (select b.valor 
          from dbContabil.cadlancamento b
		 where b.ano = 2016
           and b.mes = 01
           and b.idplano = a.codigo
       ) Janeiro2016       
  FROM dbContabil.cadplano a
order by a.tipocd desc
;