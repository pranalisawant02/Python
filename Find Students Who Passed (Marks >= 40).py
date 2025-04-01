#Q4. Find Students Who Passed (Marks >= 40)

import numpy as np

marks=[35, 60, 42, 75, 29, 90, 55]
passed_marks=[mark for mark in marks if mark>=40]
passed_students=np.array(marks)>=40
print(passed_marks)

