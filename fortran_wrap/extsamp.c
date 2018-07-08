/*  extsamp.c  */
#include <Python.h>
/* モジュールの関数 */
static PyObject *
hello(void)
{
printf("Hello World!!\n");
Py_RETURN_NONE;
}
/* モジュールのメソッドテーブル */
static PyMethodDef methods[] = {
{"hello", (PyCFunction)hello, METH_VARARGS, "print hello world.\n"},
{NULL, NULL, 0, NULL}
};
/* モジュールの初期化関数 */
PyMODINIT_FUNC
initextsamp(void)
{
(void)Py_InitModule("extsamp", methods);
}


// gcc -c extsamp.c -I C:\Users\Endo\Anaconda3\include
// ここまでは通る
// gcc -shared -o extsamp.pyd extsamp.o -L C:\Users\Endo\Anaconda3\include -l python36.lib
