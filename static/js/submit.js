function submitForm() {
if(document.registerForm.onsubmit &&
    !document.registerForm.onsubmit())
    {
        return;
    }
 document.registerForm.submit();
}
