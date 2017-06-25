from examples.expression_builder.calendar_model import Calendar


calendar = Calendar()

(calendar
    .add('Domain Specific Language tutorial')
    .on(2017, 1, 1)
    .start('10:00')
    .end('11:00')
    .at('Developers Office'))

(calendar
    .add('Domain Specific Language tutorial')
    .on(year=2017, month=1, day=2)
    .start('12:00')
    .end('13:00')
    .at('Analytics Office'))
