#메타문자는 그 문자가 가진 뜻이아니 특별한 용도로 사용하는 문자를 말한다.

#[\d] == [0-9]
#[\D] == [^0-9]
#[\s] == [ \t\n\r\f\v]
#[\S] == [^ \t\n\r\f\v]
#[\w] == [a-zA-Z0-9_]
#[\W] == [^a-zA-Z0-9_]


#Dot

#[a.b] == [a + "\n을 제외한 모든문자" + b]
#a[.]b == a + "." + b를 의미.

# * -> 반복

# ca*t --> ct cat, caat, caaaaaaaaat와 매치.

# ca+t -> ct(매치 안됨), cat, caat, caaaaat -> 매치

# {m, n} -> 반복 횟수를 정해주는 문자
# {2} -> 2번 반복
# {1, } --> + 와 동일
# {0, } --> * 과 동일
# {m, n} --> 반복횟수가 m에서 n회임.

# ? -> ab?c -> b가 있어도 되고 없어도 됨.

import re

p = re.compile("ab*")