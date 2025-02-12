import streamlit as st
import pseudointerpreter
import time

col1, col2, col3 = st.columns([0.5,0.2,0.3], gap="small")

with col1:
    code = st.text_area("Enter your pseudocode here:",height = 680)

def runcode():
    start_time = time.perf_counter()
    result, error = pseudointerpreter.run('<stdin>', code)

    if error:
        with col3:
            st.text(error.as_string())
    elif result:
        if len(result.elements) == 1:
            with col3:
                st.markdown(":blue[1|]"+" "+repr(result.elements[0]))
        else:
            with col3:
                resultlist = []
                tracker = ""
                comma_next = False
                for count in range(1,len(repr(result))-1):
                    if comma_next == True:
                        comma_next = False
                    elif repr(result)[count] != ",":
                        tracker += repr(result)[count]
                    elif repr(result)[count] == ",":
                        resultlist.append(tracker)
                        tracker = ""
                        comma_next = True
                resultlist.append(tracker)

                for count in range(0,len(resultlist)):
                    line_no = str(count+1)+"| "
                    st.markdown(f":blue[{line_no}]"+" "+resultlist[count])

    end_time = time.perf_counter()
    time_taken = (end_time-start_time)*1000
    with col3:
        "---"
        st.markdown("**Time taken:**"+" "+str(round(time_taken,3))+"ms")

with col2:
    st.button("Run", type="primary", on_click = runcode)

with col3:
    st.markdown("**Result goes here:**")