select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223456 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223457 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223458 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223459 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223460 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223461 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223462 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223470 and book=4 and lower(moviecode)='001b06242017'
group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223471 and book=4 and lower(moviecode)='001b06242017'group by `sheng` 
union all 
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas 
where chain=223472 and book=4 and lower(moviecode)='001b06242017'group by `sheng` 
union all  
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) 
from boxdatas where chain=223473 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223474 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223475 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223484 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223485 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223486 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223487 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`) from boxdatas
where chain=223488 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223490 and book=4 and lower(moviecode)='001b06242017'group by `sheng`
union all
select `sheng`, max(`showdate`), min(`showdate`), sum(`shows`), sum(`audience`), sum(`revenue`)
from boxdatas where chain=223491 and book=4 and lower(moviecode)='001b06242017'group by `sheng`

select
`chain`, `device`, `showdate_month`, sum(`shows`), sum(`audience`), sum(`revenue`) from
boxdatas where chain = 223491 and book = 4 and lower(moviecode) = '001b06242017'
group by `chain`, `device`