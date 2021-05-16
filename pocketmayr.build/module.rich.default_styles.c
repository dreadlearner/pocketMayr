/* Generated code for Python module 'rich.default_styles'
 * created by Nuitka version 0.6.14.7
 *
 * This code is in part copyright 2021 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_rich$default_styles" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_rich$default_styles;
PyDictObject *moduledict_rich$default_styles;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[211];

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("rich.default_styles"));
        constants_created = true;
    }
}

/* For multiprocessing, we want to be able to initialize the __main__ constants. */
#if (_NUITKA_PLUGIN_MULTIPROCESSING_ENABLED || _NUITKA_PLUGIN_TRACEBACK_ENCRYPTION_ENABLED) && 0
void createMainModuleConstants(void) {
    createModuleConstants();
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_rich$default_styles(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    checkConstantsBlob(&mod_consts[0], "rich.default_styles");
}
#endif

// The module code objects.
static PyCodeObject *codeobj_12dd45c01af18592233b5ff461cc59cc;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[209]); CHECK_OBJECT(module_filename_obj);
    codeobj_12dd45c01af18592233b5ff461cc59cc = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[210], NULL, NULL, 0, 0, 0);
}

// The module function declarations.


// The module function definitions.


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

function_impl_code functable_rich$default_styles[] = {

    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable_rich$default_styles;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = PyTuple_New(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = PyTuple_New(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && ERROR_OCCURRED()) {
        return NULL;
    }

    if (offset > sizeof(functable_rich$default_styles) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!ERROR_OCCURRED());

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!ERROR_OCCURRED());
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!ERROR_OCCURRED());

    PyCodeObject *code_object = MAKE_CODEOBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable_rich$default_styles[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module_rich$default_styles,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_rich$default_styles(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *module_entry) {
    module_rich$default_styles = module;

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();

#if PYTHON_VERSION < 0x300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 0x270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    PRINT_STRING("rich.default_styles: Calling setupMetaPathBasedLoader().\n");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("rich.default_styles: Calling createModuleConstants().\n");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("rich.default_styles: Calling createModuleCodeObjects().\n");
#endif
    createModuleCodeObjects();

    // PRINT_STRING("in initrich$default_styles\n");

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.

    moduledict_rich$default_styles = MODULE_DICT(module_rich$default_styles);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(module_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_rich$default_styles,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_rich$default_styles,
            (Nuitka_StringObject *)const_str_plain___package__,
            const_str_empty
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_rich$default_styles,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_rich$default_styles,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_rich$default_styles,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_rich$default_styles);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_rich$default_styles);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_rich$default_styles, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_12dd45c01af18592233b5ff461cc59cc;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_12dd45c01af18592233b5ff461cc59cc = MAKE_MODULE_FRAME(codeobj_12dd45c01af18592233b5ff461cc59cc, module_rich$default_styles);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_12dd45c01af18592233b5ff461cc59cc);
    assert(Py_REFCNT(frame_12dd45c01af18592233b5ff461cc59cc) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_name_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_name_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[2]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[3], tmp_assattr_name_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_name_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_name_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[2]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[4], tmp_assattr_name_2);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = PyDict_New();
        UPDATE_STRING_DICT1(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[6], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_name_1;
        PyObject *tmp_globals_arg_name_1;
        PyObject *tmp_locals_arg_name_1;
        PyObject *tmp_fromlist_name_1;
        PyObject *tmp_level_name_1;
        tmp_name_name_1 = mod_consts[7];
        tmp_globals_arg_name_1 = (PyObject *)moduledict_rich$default_styles;
        tmp_locals_arg_name_1 = Py_None;
        tmp_fromlist_name_1 = mod_consts[8];
        tmp_level_name_1 = mod_consts[9];
        frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 1;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_name_1, tmp_globals_arg_name_1, tmp_locals_arg_name_1, tmp_fromlist_name_1, tmp_level_name_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_5 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_rich$default_styles,
                mod_consts[10],
                mod_consts[9]
            );
        } else {
            tmp_assign_source_5 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[10]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_import_name_from_2;
        PyObject *tmp_name_name_2;
        PyObject *tmp_globals_arg_name_2;
        PyObject *tmp_locals_arg_name_2;
        PyObject *tmp_fromlist_name_2;
        PyObject *tmp_level_name_2;
        tmp_name_name_2 = mod_consts[11];
        tmp_globals_arg_name_2 = (PyObject *)moduledict_rich$default_styles;
        tmp_locals_arg_name_2 = Py_None;
        tmp_fromlist_name_2 = mod_consts[12];
        tmp_level_name_2 = mod_consts[13];
        frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 3;
        tmp_import_name_from_2 = IMPORT_MODULE5(tmp_name_name_2, tmp_globals_arg_name_2, tmp_locals_arg_name_2, tmp_fromlist_name_2, tmp_level_name_2);
        if (tmp_import_name_from_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 3;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_assign_source_6 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_2,
                (PyObject *)moduledict_rich$default_styles,
                mod_consts[14],
                mod_consts[9]
            );
        } else {
            tmp_assign_source_6 = IMPORT_NAME(tmp_import_name_from_2, mod_consts[14]);
        }

        Py_DECREF(tmp_import_name_from_2);
        if (tmp_assign_source_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 3;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        PyObject *tmp_called_instance_1;
        tmp_dict_key_1 = mod_consts[15];
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
        }

        assert(!(tmp_called_instance_1 == NULL));
        frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 7;
        tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_1, mod_consts[16]);
        if (tmp_dict_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 7;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_7 = _PyDict_NewPresized( 133 );
        {
            PyObject *tmp_called_name_1;
            PyObject *tmp_kwargs_name_1;
            PyObject *tmp_called_name_2;
            PyObject *tmp_kwargs_name_2;
            PyObject *tmp_called_name_3;
            PyObject *tmp_kwargs_name_3;
            PyObject *tmp_called_name_4;
            PyObject *tmp_kwargs_name_4;
            PyObject *tmp_called_name_5;
            PyObject *tmp_kwargs_name_5;
            PyObject *tmp_called_name_6;
            PyObject *tmp_kwargs_name_6;
            PyObject *tmp_called_name_7;
            PyObject *tmp_kwargs_name_7;
            PyObject *tmp_called_name_8;
            PyObject *tmp_kwargs_name_8;
            PyObject *tmp_called_name_9;
            PyObject *tmp_kwargs_name_9;
            PyObject *tmp_called_name_10;
            PyObject *tmp_kwargs_name_10;
            PyObject *tmp_called_name_11;
            PyObject *tmp_kwargs_name_11;
            PyObject *tmp_called_name_12;
            PyObject *tmp_kwargs_name_12;
            PyObject *tmp_called_name_13;
            PyObject *tmp_kwargs_name_13;
            PyObject *tmp_called_name_14;
            PyObject *tmp_kwargs_name_14;
            PyObject *tmp_called_name_15;
            PyObject *tmp_kwargs_name_15;
            PyObject *tmp_called_name_16;
            PyObject *tmp_kwargs_name_16;
            PyObject *tmp_called_name_17;
            PyObject *tmp_kwargs_name_17;
            PyObject *tmp_called_name_18;
            PyObject *tmp_kwargs_name_18;
            PyObject *tmp_called_name_19;
            PyObject *tmp_kwargs_name_19;
            PyObject *tmp_called_name_20;
            PyObject *tmp_kwargs_name_20;
            PyObject *tmp_called_name_21;
            PyObject *tmp_kwargs_name_21;
            PyObject *tmp_called_name_22;
            PyObject *tmp_kwargs_name_22;
            PyObject *tmp_called_name_23;
            PyObject *tmp_kwargs_name_23;
            PyObject *tmp_called_name_24;
            PyObject *tmp_kwargs_name_24;
            PyObject *tmp_called_name_25;
            PyObject *tmp_kwargs_name_25;
            PyObject *tmp_called_name_26;
            PyObject *tmp_called_name_27;
            PyObject *tmp_kwargs_name_26;
            PyObject *tmp_called_name_28;
            PyObject *tmp_kwargs_name_27;
            PyObject *tmp_called_name_29;
            PyObject *tmp_kwargs_name_28;
            PyObject *tmp_called_name_30;
            PyObject *tmp_kwargs_name_29;
            PyObject *tmp_called_name_31;
            PyObject *tmp_kwargs_name_30;
            PyObject *tmp_called_name_32;
            PyObject *tmp_kwargs_name_31;
            PyObject *tmp_called_name_33;
            PyObject *tmp_kwargs_name_32;
            PyObject *tmp_called_name_34;
            PyObject *tmp_kwargs_name_33;
            PyObject *tmp_called_name_35;
            PyObject *tmp_kwargs_name_34;
            PyObject *tmp_called_name_36;
            PyObject *tmp_kwargs_name_35;
            PyObject *tmp_called_name_37;
            PyObject *tmp_kwargs_name_36;
            PyObject *tmp_called_name_38;
            PyObject *tmp_kwargs_name_37;
            PyObject *tmp_called_name_39;
            PyObject *tmp_kwargs_name_38;
            PyObject *tmp_called_instance_2;
            PyObject *tmp_called_name_40;
            PyObject *tmp_kwargs_name_39;
            PyObject *tmp_called_instance_3;
            PyObject *tmp_called_name_41;
            PyObject *tmp_kwargs_name_40;
            PyObject *tmp_called_name_42;
            PyObject *tmp_kwargs_name_41;
            PyObject *tmp_called_name_43;
            PyObject *tmp_kwargs_name_42;
            PyObject *tmp_called_name_44;
            PyObject *tmp_kwargs_name_43;
            PyObject *tmp_called_name_45;
            PyObject *tmp_kwargs_name_44;
            PyObject *tmp_called_name_46;
            PyObject *tmp_kwargs_name_45;
            PyObject *tmp_called_name_47;
            PyObject *tmp_kwargs_name_46;
            PyObject *tmp_called_name_48;
            PyObject *tmp_kwargs_name_47;
            PyObject *tmp_called_name_49;
            PyObject *tmp_kwargs_name_48;
            PyObject *tmp_called_name_50;
            PyObject *tmp_kwargs_name_49;
            PyObject *tmp_called_name_51;
            PyObject *tmp_kwargs_name_50;
            PyObject *tmp_called_name_52;
            PyObject *tmp_kwargs_name_51;
            PyObject *tmp_called_name_53;
            PyObject *tmp_kwargs_name_52;
            PyObject *tmp_called_name_54;
            PyObject *tmp_kwargs_name_53;
            PyObject *tmp_called_name_55;
            PyObject *tmp_kwargs_name_54;
            PyObject *tmp_called_name_56;
            PyObject *tmp_kwargs_name_55;
            PyObject *tmp_called_name_57;
            PyObject *tmp_kwargs_name_56;
            PyObject *tmp_called_name_58;
            PyObject *tmp_kwargs_name_57;
            PyObject *tmp_called_name_59;
            PyObject *tmp_kwargs_name_58;
            PyObject *tmp_called_name_60;
            PyObject *tmp_kwargs_name_59;
            PyObject *tmp_called_name_61;
            PyObject *tmp_kwargs_name_60;
            PyObject *tmp_called_name_62;
            PyObject *tmp_kwargs_name_61;
            PyObject *tmp_called_name_63;
            PyObject *tmp_kwargs_name_62;
            PyObject *tmp_called_name_64;
            PyObject *tmp_kwargs_name_63;
            PyObject *tmp_called_name_65;
            PyObject *tmp_kwargs_name_64;
            PyObject *tmp_called_name_66;
            PyObject *tmp_kwargs_name_65;
            PyObject *tmp_called_name_67;
            PyObject *tmp_kwargs_name_66;
            PyObject *tmp_called_name_68;
            PyObject *tmp_kwargs_name_67;
            PyObject *tmp_called_instance_4;
            PyObject *tmp_called_instance_5;
            PyObject *tmp_called_name_69;
            PyObject *tmp_kwargs_name_68;
            PyObject *tmp_called_name_70;
            PyObject *tmp_kwargs_name_69;
            PyObject *tmp_called_name_71;
            PyObject *tmp_kwargs_name_70;
            PyObject *tmp_called_name_72;
            PyObject *tmp_kwargs_name_71;
            PyObject *tmp_called_instance_6;
            PyObject *tmp_called_name_73;
            PyObject *tmp_kwargs_name_72;
            PyObject *tmp_called_name_74;
            PyObject *tmp_kwargs_name_73;
            PyObject *tmp_called_name_75;
            PyObject *tmp_kwargs_name_74;
            PyObject *tmp_called_name_76;
            PyObject *tmp_kwargs_name_75;
            PyObject *tmp_called_name_77;
            PyObject *tmp_kwargs_name_76;
            PyObject *tmp_called_name_78;
            PyObject *tmp_kwargs_name_77;
            PyObject *tmp_called_instance_7;
            PyObject *tmp_called_name_79;
            PyObject *tmp_kwargs_name_78;
            PyObject *tmp_called_name_80;
            PyObject *tmp_kwargs_name_79;
            PyObject *tmp_called_name_81;
            PyObject *tmp_kwargs_name_80;
            PyObject *tmp_called_name_82;
            PyObject *tmp_kwargs_name_81;
            PyObject *tmp_called_name_83;
            PyObject *tmp_kwargs_name_82;
            PyObject *tmp_called_instance_8;
            PyObject *tmp_called_name_84;
            PyObject *tmp_kwargs_name_83;
            PyObject *tmp_called_name_85;
            PyObject *tmp_kwargs_name_84;
            PyObject *tmp_called_instance_9;
            PyObject *tmp_called_name_86;
            PyObject *tmp_kwargs_name_85;
            PyObject *tmp_called_name_87;
            PyObject *tmp_kwargs_name_86;
            PyObject *tmp_called_name_88;
            PyObject *tmp_kwargs_name_87;
            PyObject *tmp_called_name_89;
            PyObject *tmp_kwargs_name_88;
            PyObject *tmp_called_name_90;
            PyObject *tmp_kwargs_name_89;
            PyObject *tmp_called_instance_10;
            PyObject *tmp_called_name_91;
            PyObject *tmp_kwargs_name_90;
            PyObject *tmp_called_name_92;
            PyObject *tmp_kwargs_name_91;
            PyObject *tmp_called_name_93;
            PyObject *tmp_kwargs_name_92;
            PyObject *tmp_called_name_94;
            PyObject *tmp_kwargs_name_93;
            PyObject *tmp_called_name_95;
            PyObject *tmp_kwargs_name_94;
            PyObject *tmp_called_name_96;
            PyObject *tmp_kwargs_name_95;
            PyObject *tmp_called_name_97;
            PyObject *tmp_kwargs_name_96;
            PyObject *tmp_called_name_98;
            PyObject *tmp_kwargs_name_97;
            PyObject *tmp_called_name_99;
            PyObject *tmp_kwargs_name_98;
            PyObject *tmp_called_name_100;
            PyObject *tmp_called_name_101;
            PyObject *tmp_called_name_102;
            PyObject *tmp_called_name_103;
            PyObject *tmp_called_name_104;
            PyObject *tmp_kwargs_name_99;
            PyObject *tmp_called_name_105;
            PyObject *tmp_kwargs_name_100;
            PyObject *tmp_called_name_106;
            PyObject *tmp_kwargs_name_101;
            PyObject *tmp_called_name_107;
            PyObject *tmp_kwargs_name_102;
            PyObject *tmp_called_name_108;
            PyObject *tmp_kwargs_name_103;
            PyObject *tmp_called_name_109;
            PyObject *tmp_kwargs_name_104;
            PyObject *tmp_called_name_110;
            PyObject *tmp_called_name_111;
            PyObject *tmp_kwargs_name_105;
            PyObject *tmp_called_name_112;
            PyObject *tmp_kwargs_name_106;
            PyObject *tmp_called_name_113;
            PyObject *tmp_kwargs_name_107;
            PyObject *tmp_called_name_114;
            PyObject *tmp_called_name_115;
            PyObject *tmp_kwargs_name_108;
            PyObject *tmp_called_name_116;
            PyObject *tmp_kwargs_name_109;
            PyObject *tmp_called_name_117;
            PyObject *tmp_kwargs_name_110;
            PyObject *tmp_called_name_118;
            PyObject *tmp_kwargs_name_111;
            PyObject *tmp_called_name_119;
            PyObject *tmp_kwargs_name_112;
            PyObject *tmp_called_name_120;
            PyObject *tmp_kwargs_name_113;
            PyObject *tmp_called_name_121;
            PyObject *tmp_kwargs_name_114;
            PyObject *tmp_called_name_122;
            PyObject *tmp_kwargs_name_115;
            PyObject *tmp_called_name_123;
            PyObject *tmp_kwargs_name_116;
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[17];
            tmp_called_name_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_1 == NULL)) {
                tmp_called_name_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 8;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_1 = PyDict_Copy(mod_consts[18]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 8;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_1, tmp_kwargs_name_1);
            Py_DECREF(tmp_kwargs_name_1);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 8;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[19];
            tmp_called_name_2 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_2 == NULL)) {
                tmp_called_name_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 21;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_2 = PyDict_Copy(mod_consts[20]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 21;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_2, tmp_kwargs_name_2);
            Py_DECREF(tmp_kwargs_name_2);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 21;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[21];
            tmp_called_name_3 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_3 == NULL)) {
                tmp_called_name_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 22;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_3 = PyDict_Copy(mod_consts[22]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 22;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_3, tmp_kwargs_name_3);
            Py_DECREF(tmp_kwargs_name_3);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 22;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[23];
            tmp_called_name_4 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_4 == NULL)) {
                tmp_called_name_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 23;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_4 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 23;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_4, tmp_kwargs_name_4);
            Py_DECREF(tmp_kwargs_name_4);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 23;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[25];
            tmp_called_name_5 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_5 == NULL)) {
                tmp_called_name_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 24;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_5 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 24;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_5, tmp_kwargs_name_5);
            Py_DECREF(tmp_kwargs_name_5);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 24;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[26];
            tmp_called_name_6 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_6 == NULL)) {
                tmp_called_name_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 25;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_6 = PyDict_Copy(mod_consts[27]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 25;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_6, tmp_kwargs_name_6);
            Py_DECREF(tmp_kwargs_name_6);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 25;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[28];
            tmp_called_name_7 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_7 == NULL)) {
                tmp_called_name_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 26;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_7 = PyDict_Copy(mod_consts[29]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 26;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_7, tmp_kwargs_name_7);
            Py_DECREF(tmp_kwargs_name_7);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 26;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[30];
            tmp_called_name_8 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_8 == NULL)) {
                tmp_called_name_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 27;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_8 = PyDict_Copy(mod_consts[29]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 27;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_8, tmp_kwargs_name_8);
            Py_DECREF(tmp_kwargs_name_8);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 27;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[31];
            tmp_called_name_9 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_9 == NULL)) {
                tmp_called_name_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 28;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_9 = PyDict_Copy(mod_consts[32]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 28;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_9, tmp_kwargs_name_9);
            Py_DECREF(tmp_kwargs_name_9);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 28;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[33];
            tmp_called_name_10 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_10 == NULL)) {
                tmp_called_name_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 29;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_10 = PyDict_Copy(mod_consts[34]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 29;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_10, tmp_kwargs_name_10);
            Py_DECREF(tmp_kwargs_name_10);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 29;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[35];
            tmp_called_name_11 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_11 == NULL)) {
                tmp_called_name_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_11 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 30;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_11 = PyDict_Copy(mod_consts[36]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 30;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_11, tmp_kwargs_name_11);
            Py_DECREF(tmp_kwargs_name_11);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 30;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[37];
            tmp_called_name_12 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_12 == NULL)) {
                tmp_called_name_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_12 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 31;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_12 = PyDict_Copy(mod_consts[38]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 31;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_12, tmp_kwargs_name_12);
            Py_DECREF(tmp_kwargs_name_12);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 31;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[39];
            tmp_called_name_13 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_13 == NULL)) {
                tmp_called_name_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 32;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_13 = PyDict_Copy(mod_consts[40]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 32;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_13, tmp_kwargs_name_13);
            Py_DECREF(tmp_kwargs_name_13);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 32;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[41];
            tmp_called_name_14 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_14 == NULL)) {
                tmp_called_name_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 33;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_14 = PyDict_Copy(mod_consts[42]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 33;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_14, tmp_kwargs_name_14);
            Py_DECREF(tmp_kwargs_name_14);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 33;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[43];
            tmp_called_name_15 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_15 == NULL)) {
                tmp_called_name_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_15 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 34;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_15, tmp_kwargs_name_15);
            Py_DECREF(tmp_kwargs_name_15);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[45];
            tmp_called_name_16 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_16 == NULL)) {
                tmp_called_name_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_16 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 35;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_16 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 35;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_16, tmp_kwargs_name_16);
            Py_DECREF(tmp_kwargs_name_16);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 35;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[47];
            tmp_called_name_17 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_17 == NULL)) {
                tmp_called_name_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 36;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_17 = PyDict_Copy(mod_consts[48]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 36;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_17, tmp_kwargs_name_17);
            Py_DECREF(tmp_kwargs_name_17);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 36;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[49];
            tmp_called_name_18 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_18 == NULL)) {
                tmp_called_name_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_18 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 37;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_18 = PyDict_Copy(mod_consts[50]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 37;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_18, tmp_kwargs_name_18);
            Py_DECREF(tmp_kwargs_name_18);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 37;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[51];
            tmp_called_name_19 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_19 == NULL)) {
                tmp_called_name_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_19 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 38;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_19 = PyDict_Copy(mod_consts[52]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 38;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_19, tmp_kwargs_name_19);
            Py_DECREF(tmp_kwargs_name_19);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 38;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[53];
            tmp_called_name_20 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_20 == NULL)) {
                tmp_called_name_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 39;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_20 = PyDict_Copy(mod_consts[54]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 39;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_20, tmp_kwargs_name_20);
            Py_DECREF(tmp_kwargs_name_20);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 39;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[55];
            tmp_called_name_21 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_21 == NULL)) {
                tmp_called_name_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 40;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_21 = PyDict_Copy(mod_consts[56]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 40;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_21, tmp_kwargs_name_21);
            Py_DECREF(tmp_kwargs_name_21);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 40;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[57];
            tmp_called_name_22 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_22 == NULL)) {
                tmp_called_name_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 41;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_22 = PyDict_Copy(mod_consts[58]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 41;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_22, tmp_kwargs_name_22);
            Py_DECREF(tmp_kwargs_name_22);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 41;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[59];
            tmp_called_name_23 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_23 == NULL)) {
                tmp_called_name_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 42;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_23 = PyDict_Copy(mod_consts[60]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 42;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_23, tmp_kwargs_name_23);
            Py_DECREF(tmp_kwargs_name_23);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 42;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[61];
            tmp_called_name_24 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_24 == NULL)) {
                tmp_called_name_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 43;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_24 = PyDict_Copy(mod_consts[62]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 43;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_24, tmp_kwargs_name_24);
            Py_DECREF(tmp_kwargs_name_24);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 43;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[63];
            tmp_called_name_25 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_25 == NULL)) {
                tmp_called_name_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_25 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 44;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_25 = PyDict_Copy(mod_consts[60]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 44;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_25, tmp_kwargs_name_25);
            Py_DECREF(tmp_kwargs_name_25);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 44;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[64];
            tmp_called_name_26 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_26 == NULL)) {
                tmp_called_name_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 45;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 45;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_26);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 45;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[65];
            tmp_called_name_27 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_27 == NULL)) {
                tmp_called_name_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_27 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 46;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_26 = PyDict_Copy(mod_consts[52]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 46;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_27, tmp_kwargs_name_26);
            Py_DECREF(tmp_kwargs_name_26);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 46;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[66];
            tmp_called_name_28 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_28 == NULL)) {
                tmp_called_name_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 47;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_27 = PyDict_Copy(mod_consts[20]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 47;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_28, tmp_kwargs_name_27);
            Py_DECREF(tmp_kwargs_name_27);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 47;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[67];
            tmp_called_name_29 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_29 == NULL)) {
                tmp_called_name_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_29 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 48;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_28 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 48;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_29, tmp_kwargs_name_28);
            Py_DECREF(tmp_kwargs_name_28);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 48;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[68];
            tmp_called_name_30 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_30 == NULL)) {
                tmp_called_name_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 49;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_29 = PyDict_Copy(mod_consts[60]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 49;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_30, tmp_kwargs_name_29);
            Py_DECREF(tmp_kwargs_name_29);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 49;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[69];
            tmp_called_name_31 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_31 == NULL)) {
                tmp_called_name_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 50;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_30 = PyDict_Copy(mod_consts[70]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 50;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_31, tmp_kwargs_name_30);
            Py_DECREF(tmp_kwargs_name_30);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 50;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[71];
            tmp_called_name_32 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_32 == NULL)) {
                tmp_called_name_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_32 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_31 = PyDict_Copy(mod_consts[72]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 51;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_32, tmp_kwargs_name_31);
            Py_DECREF(tmp_kwargs_name_31);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[73];
            tmp_called_name_33 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_33 == NULL)) {
                tmp_called_name_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 52;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_32 = PyDict_Copy(mod_consts[74]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 52;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_33, tmp_kwargs_name_32);
            Py_DECREF(tmp_kwargs_name_32);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 52;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[75];
            tmp_called_name_34 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_34 == NULL)) {
                tmp_called_name_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_34 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 53;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_33 = PyDict_Copy(mod_consts[20]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 53;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_34, tmp_kwargs_name_33);
            Py_DECREF(tmp_kwargs_name_33);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 53;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[76];
            tmp_called_name_35 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_35 == NULL)) {
                tmp_called_name_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_35 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_34 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 54;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_35, tmp_kwargs_name_34);
            Py_DECREF(tmp_kwargs_name_34);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[77];
            tmp_called_name_36 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_36 == NULL)) {
                tmp_called_name_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_36 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 55;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_35 = PyDict_Copy(mod_consts[78]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 55;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_36, tmp_kwargs_name_35);
            Py_DECREF(tmp_kwargs_name_35);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 55;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[79];
            tmp_called_name_37 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_37 == NULL)) {
                tmp_called_name_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_37 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 56;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_36 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 56;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_37, tmp_kwargs_name_36);
            Py_DECREF(tmp_kwargs_name_36);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 56;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[80];
            tmp_called_name_38 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_38 == NULL)) {
                tmp_called_name_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_38 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 57;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_37 = PyDict_Copy(mod_consts[81]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 57;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_38, tmp_kwargs_name_37);
            Py_DECREF(tmp_kwargs_name_37);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 57;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[82];
            tmp_called_name_39 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_39 == NULL)) {
                tmp_called_name_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_39 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 58;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_38 = PyDict_Copy(mod_consts[83]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 58;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_39, tmp_kwargs_name_38);
            Py_DECREF(tmp_kwargs_name_38);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 58;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[84];
            tmp_called_instance_2 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_2 == NULL)) {
                tmp_called_instance_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 59;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 59;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_2, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 59;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[85];
            tmp_called_name_40 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_40 == NULL)) {
                tmp_called_name_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_40 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 60;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_39 = PyDict_Copy(mod_consts[86]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 60;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_40, tmp_kwargs_name_39);
            Py_DECREF(tmp_kwargs_name_39);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 60;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[87];
            tmp_called_instance_3 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_3 == NULL)) {
                tmp_called_instance_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 61;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 61;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_3, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 61;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[88];
            tmp_called_name_41 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_41 == NULL)) {
                tmp_called_name_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_41 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 62;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_40 = PyDict_Copy(mod_consts[20]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 62;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_41, tmp_kwargs_name_40);
            Py_DECREF(tmp_kwargs_name_40);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 62;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[89];
            tmp_called_name_42 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_42 == NULL)) {
                tmp_called_name_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_42 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_41 = PyDict_Copy(mod_consts[48]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 63;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_42, tmp_kwargs_name_41);
            Py_DECREF(tmp_kwargs_name_41);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[90];
            tmp_called_name_43 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_43 == NULL)) {
                tmp_called_name_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_43 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 64;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_42 = PyDict_Copy(mod_consts[91]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 64;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_43, tmp_kwargs_name_42);
            Py_DECREF(tmp_kwargs_name_42);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 64;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[92];
            tmp_called_name_44 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_44 == NULL)) {
                tmp_called_name_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_44 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 65;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_43 = PyDict_Copy(mod_consts[81]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 65;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_44, tmp_kwargs_name_43);
            Py_DECREF(tmp_kwargs_name_43);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 65;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[93];
            tmp_called_name_45 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_45 == NULL)) {
                tmp_called_name_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_45 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 66;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_44 = PyDict_Copy(mod_consts[94]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 66;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_45, tmp_kwargs_name_44);
            Py_DECREF(tmp_kwargs_name_44);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 66;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[95];
            tmp_called_name_46 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_46 == NULL)) {
                tmp_called_name_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_46 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_45 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 67;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_46, tmp_kwargs_name_45);
            Py_DECREF(tmp_kwargs_name_45);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[96];
            tmp_called_name_47 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_47 == NULL)) {
                tmp_called_name_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_47 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 68;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_46 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 68;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_47, tmp_kwargs_name_46);
            Py_DECREF(tmp_kwargs_name_46);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 68;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[97];
            tmp_called_name_48 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_48 == NULL)) {
                tmp_called_name_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_48 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_47 = PyDict_Copy(mod_consts[98]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 69;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_48, tmp_kwargs_name_47);
            Py_DECREF(tmp_kwargs_name_47);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[99];
            tmp_called_name_49 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_49 == NULL)) {
                tmp_called_name_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_49 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 70;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_48 = PyDict_Copy(mod_consts[98]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 70;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_49, tmp_kwargs_name_48);
            Py_DECREF(tmp_kwargs_name_48);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 70;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[100];
            tmp_called_name_50 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_50 == NULL)) {
                tmp_called_name_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_50 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 71;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_49 = PyDict_Copy(mod_consts[98]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 71;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_50, tmp_kwargs_name_49);
            Py_DECREF(tmp_kwargs_name_49);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 71;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[101];
            tmp_called_name_51 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_51 == NULL)) {
                tmp_called_name_51 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_51 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_50 = PyDict_Copy(mod_consts[98]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 72;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_51, tmp_kwargs_name_50);
            Py_DECREF(tmp_kwargs_name_50);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[102];
            tmp_called_name_52 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_52 == NULL)) {
                tmp_called_name_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_52 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_51 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 73;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_52, tmp_kwargs_name_51);
            Py_DECREF(tmp_kwargs_name_51);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[103];
            tmp_called_name_53 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_53 == NULL)) {
                tmp_called_name_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_53 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 74;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_52 = PyDict_Copy(mod_consts[104]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 74;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_53, tmp_kwargs_name_52);
            Py_DECREF(tmp_kwargs_name_52);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 74;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[105];
            tmp_called_name_54 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_54 == NULL)) {
                tmp_called_name_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_54 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 75;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_53 = PyDict_Copy(mod_consts[106]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 75;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_54, tmp_kwargs_name_53);
            Py_DECREF(tmp_kwargs_name_53);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 75;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[107];
            tmp_called_name_55 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_55 == NULL)) {
                tmp_called_name_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_55 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 76;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_54 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 76;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_55, tmp_kwargs_name_54);
            Py_DECREF(tmp_kwargs_name_54);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 76;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[108];
            tmp_called_name_56 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_56 == NULL)) {
                tmp_called_name_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_56 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_55 = PyDict_Copy(mod_consts[109]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 77;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_56, tmp_kwargs_name_55);
            Py_DECREF(tmp_kwargs_name_55);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[110];
            tmp_called_name_57 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_57 == NULL)) {
                tmp_called_name_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_57 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 78;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_56 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 78;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_57, tmp_kwargs_name_56);
            Py_DECREF(tmp_kwargs_name_56);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 78;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[111];
            tmp_called_name_58 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_58 == NULL)) {
                tmp_called_name_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_58 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 79;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_57 = PyDict_Copy(mod_consts[112]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 79;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_58, tmp_kwargs_name_57);
            Py_DECREF(tmp_kwargs_name_57);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 79;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[113];
            tmp_called_name_59 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_59 == NULL)) {
                tmp_called_name_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_59 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 80;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_58 = PyDict_Copy(mod_consts[114]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 80;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_59, tmp_kwargs_name_58);
            Py_DECREF(tmp_kwargs_name_58);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 80;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[115];
            tmp_called_name_60 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_60 == NULL)) {
                tmp_called_name_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_60 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 81;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_59 = PyDict_Copy(mod_consts[116]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 81;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_60, tmp_kwargs_name_59);
            Py_DECREF(tmp_kwargs_name_59);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 81;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[117];
            tmp_called_name_61 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_61 == NULL)) {
                tmp_called_name_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_61 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_60 = PyDict_Copy(mod_consts[118]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 82;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_61, tmp_kwargs_name_60);
            Py_DECREF(tmp_kwargs_name_60);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[119];
            tmp_called_name_62 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_62 == NULL)) {
                tmp_called_name_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_62 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 83;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_61 = PyDict_Copy(mod_consts[120]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 83;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_62, tmp_kwargs_name_61);
            Py_DECREF(tmp_kwargs_name_61);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 83;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[121];
            tmp_called_name_63 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_63 == NULL)) {
                tmp_called_name_63 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_63 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_62 = PyDict_Copy(mod_consts[122]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 84;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_63, tmp_kwargs_name_62);
            Py_DECREF(tmp_kwargs_name_62);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[123];
            tmp_called_name_64 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_64 == NULL)) {
                tmp_called_name_64 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_64 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 85;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_63 = PyDict_Copy(mod_consts[124]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 85;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_64, tmp_kwargs_name_63);
            Py_DECREF(tmp_kwargs_name_63);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 85;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[125];
            tmp_called_name_65 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_65 == NULL)) {
                tmp_called_name_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_65 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 86;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_64 = PyDict_Copy(mod_consts[126]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 86;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_65, tmp_kwargs_name_64);
            Py_DECREF(tmp_kwargs_name_64);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 86;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[127];
            tmp_called_name_66 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_66 == NULL)) {
                tmp_called_name_66 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_66 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 87;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_65 = PyDict_Copy(mod_consts[50]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 87;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_66, tmp_kwargs_name_65);
            Py_DECREF(tmp_kwargs_name_65);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 87;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[128];
            tmp_called_name_67 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_67 == NULL)) {
                tmp_called_name_67 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_67 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 88;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_66 = PyDict_Copy(mod_consts[129]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 88;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_67, tmp_kwargs_name_66);
            Py_DECREF(tmp_kwargs_name_66);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 88;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[130];
            tmp_called_name_68 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_68 == NULL)) {
                tmp_called_name_68 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_68 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 89;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_67 = PyDict_Copy(mod_consts[131]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 89;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_68, tmp_kwargs_name_67);
            Py_DECREF(tmp_kwargs_name_67);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 89;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[132];
            tmp_called_instance_4 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_4 == NULL)) {
                tmp_called_instance_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 90;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 90;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_4, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 90;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[133];
            tmp_called_instance_5 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_5 == NULL)) {
                tmp_called_instance_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 91;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 91;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_5, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 91;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[134];
            tmp_called_name_69 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_69 == NULL)) {
                tmp_called_name_69 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_69 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 92;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_68 = PyDict_Copy(mod_consts[126]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 92;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_69, tmp_kwargs_name_68);
            Py_DECREF(tmp_kwargs_name_68);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 92;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[135];
            tmp_called_name_70 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_70 == NULL)) {
                tmp_called_name_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_70 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 93;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_69 = PyDict_Copy(mod_consts[136]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 93;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_70, tmp_kwargs_name_69);
            Py_DECREF(tmp_kwargs_name_69);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 93;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[137];
            tmp_called_name_71 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_71 == NULL)) {
                tmp_called_name_71 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_71 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 94;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_70 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 94;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_71, tmp_kwargs_name_70);
            Py_DECREF(tmp_kwargs_name_70);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 94;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[138];
            tmp_called_name_72 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_72 == NULL)) {
                tmp_called_name_72 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_72 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 95;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_71 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 95;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_72, tmp_kwargs_name_71);
            Py_DECREF(tmp_kwargs_name_71);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 95;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[139];
            tmp_called_instance_6 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_6 == NULL)) {
                tmp_called_instance_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 96;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 96;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_6, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 96;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[140];
            tmp_called_name_73 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_73 == NULL)) {
                tmp_called_name_73 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_73 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 97;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_72 = PyDict_Copy(mod_consts[78]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 97;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_73, tmp_kwargs_name_72);
            Py_DECREF(tmp_kwargs_name_72);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 97;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[141];
            tmp_called_name_74 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_74 == NULL)) {
                tmp_called_name_74 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_74 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 98;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_73 = PyDict_Copy(mod_consts[56]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 98;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_74, tmp_kwargs_name_73);
            Py_DECREF(tmp_kwargs_name_73);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 98;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[142];
            tmp_called_name_75 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_75 == NULL)) {
                tmp_called_name_75 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_75 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 99;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_74 = PyDict_Copy(mod_consts[58]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 99;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_75, tmp_kwargs_name_74);
            Py_DECREF(tmp_kwargs_name_74);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 99;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[143];
            tmp_called_name_76 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_76 == NULL)) {
                tmp_called_name_76 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_76 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 100;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_75 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 100;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_76, tmp_kwargs_name_75);
            Py_DECREF(tmp_kwargs_name_75);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 100;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[144];
            tmp_called_name_77 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_77 == NULL)) {
                tmp_called_name_77 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_77 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_76 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 101;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_77, tmp_kwargs_name_76);
            Py_DECREF(tmp_kwargs_name_76);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[145];
            tmp_called_name_78 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_78 == NULL)) {
                tmp_called_name_78 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_78 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_77 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 102;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_78, tmp_kwargs_name_77);
            Py_DECREF(tmp_kwargs_name_77);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[146];
            tmp_called_instance_7 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_7 == NULL)) {
                tmp_called_instance_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 103;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 103;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_7, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 103;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[147];
            tmp_called_name_79 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_79 == NULL)) {
                tmp_called_name_79 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_79 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 104;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_78 = PyDict_Copy(mod_consts[29]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 104;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_79, tmp_kwargs_name_78);
            Py_DECREF(tmp_kwargs_name_78);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 104;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[148];
            tmp_called_name_80 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_80 == NULL)) {
                tmp_called_name_80 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_80 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 105;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_79 = PyDict_Copy(mod_consts[149]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 105;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_80, tmp_kwargs_name_79);
            Py_DECREF(tmp_kwargs_name_79);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 105;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[150];
            tmp_called_name_81 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_81 == NULL)) {
                tmp_called_name_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_81 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 106;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_80 = PyDict_Copy(mod_consts[151]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 106;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_81, tmp_kwargs_name_80);
            Py_DECREF(tmp_kwargs_name_80);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 106;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[152];
            tmp_called_name_82 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_82 == NULL)) {
                tmp_called_name_82 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_82 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 107;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_81 = PyDict_Copy(mod_consts[153]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 107;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_82, tmp_kwargs_name_81);
            Py_DECREF(tmp_kwargs_name_81);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 107;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[154];
            tmp_called_name_83 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_83 == NULL)) {
                tmp_called_name_83 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_83 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 108;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_82 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 108;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_83, tmp_kwargs_name_82);
            Py_DECREF(tmp_kwargs_name_82);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 108;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[155];
            tmp_called_instance_8 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_8 == NULL)) {
                tmp_called_instance_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 109;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 109;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_8, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 109;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[156];
            tmp_called_name_84 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_84 == NULL)) {
                tmp_called_name_84 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_84 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 110;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_83 = PyDict_Copy(mod_consts[81]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 110;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_84, tmp_kwargs_name_83);
            Py_DECREF(tmp_kwargs_name_83);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 110;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[157];
            tmp_called_name_85 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_85 == NULL)) {
                tmp_called_name_85 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_85 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 111;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_84 = PyDict_Copy(mod_consts[158]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 111;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_85, tmp_kwargs_name_84);
            Py_DECREF(tmp_kwargs_name_84);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 111;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[159];
            tmp_called_instance_9 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_9 == NULL)) {
                tmp_called_instance_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 112;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 112;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_9, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 112;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[160];
            tmp_called_name_86 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_86 == NULL)) {
                tmp_called_name_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_86 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 113;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_85 = PyDict_Copy(mod_consts[158]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 113;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_86, tmp_kwargs_name_85);
            Py_DECREF(tmp_kwargs_name_85);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 113;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[161];
            tmp_called_name_87 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_87 == NULL)) {
                tmp_called_name_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_87 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 114;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_86 = PyDict_Copy(mod_consts[162]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 114;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_87, tmp_kwargs_name_86);
            Py_DECREF(tmp_kwargs_name_86);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 114;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[163];
            tmp_called_name_88 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_88 == NULL)) {
                tmp_called_name_88 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_88 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 115;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_87 = PyDict_Copy(mod_consts[164]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 115;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_88, tmp_kwargs_name_87);
            Py_DECREF(tmp_kwargs_name_87);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 115;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[165];
            tmp_called_name_89 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_89 == NULL)) {
                tmp_called_name_89 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_89 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 116;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_88 = PyDict_Copy(mod_consts[166]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 116;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_89, tmp_kwargs_name_88);
            Py_DECREF(tmp_kwargs_name_88);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 116;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[167];
            tmp_called_name_90 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_90 == NULL)) {
                tmp_called_name_90 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_90 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 117;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_89 = PyDict_Copy(mod_consts[164]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 117;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_90, tmp_kwargs_name_89);
            Py_DECREF(tmp_kwargs_name_89);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 117;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[168];
            tmp_called_instance_10 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_instance_10 == NULL)) {
                tmp_called_instance_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_instance_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 118;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 118;
            tmp_dict_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_10, mod_consts[16]);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 118;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[169];
            tmp_called_name_91 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_91 == NULL)) {
                tmp_called_name_91 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_91 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 119;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_90 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 119;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_91, tmp_kwargs_name_90);
            Py_DECREF(tmp_kwargs_name_90);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 119;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[170];
            tmp_called_name_92 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_92 == NULL)) {
                tmp_called_name_92 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_92 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 120;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_91 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 120;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_92, tmp_kwargs_name_91);
            Py_DECREF(tmp_kwargs_name_91);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 120;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[171];
            tmp_called_name_93 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_93 == NULL)) {
                tmp_called_name_93 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_93 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 121;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_92 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 121;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_93, tmp_kwargs_name_92);
            Py_DECREF(tmp_kwargs_name_92);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 121;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[172];
            tmp_called_name_94 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_94 == NULL)) {
                tmp_called_name_94 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_94 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 122;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_93 = PyDict_Copy(mod_consts[48]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 122;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_94, tmp_kwargs_name_93);
            Py_DECREF(tmp_kwargs_name_93);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 122;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[173];
            tmp_called_name_95 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_95 == NULL)) {
                tmp_called_name_95 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_95 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 123;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_94 = PyDict_Copy(mod_consts[50]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 123;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_95, tmp_kwargs_name_94);
            Py_DECREF(tmp_kwargs_name_94);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 123;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[174];
            tmp_called_name_96 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_96 == NULL)) {
                tmp_called_name_96 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_96 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 124;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_95 = PyDict_Copy(mod_consts[52]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 124;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_96, tmp_kwargs_name_95);
            Py_DECREF(tmp_kwargs_name_95);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 124;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[175];
            tmp_called_name_97 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_97 == NULL)) {
                tmp_called_name_97 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_97 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 125;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_96 = PyDict_Copy(mod_consts[44]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 125;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_97, tmp_kwargs_name_96);
            Py_DECREF(tmp_kwargs_name_96);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 125;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[176];
            tmp_called_name_98 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_98 == NULL)) {
                tmp_called_name_98 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_98 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 126;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_97 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 126;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_98, tmp_kwargs_name_97);
            Py_DECREF(tmp_kwargs_name_97);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 126;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[177];
            tmp_called_name_99 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_99 == NULL)) {
                tmp_called_name_99 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_99 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 127;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_98 = PyDict_Copy(mod_consts[46]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 127;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_99, tmp_kwargs_name_98);
            Py_DECREF(tmp_kwargs_name_98);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 127;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[178];
            tmp_called_name_100 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_100 == NULL)) {
                tmp_called_name_100 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_100 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 128;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 128;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_100);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 128;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[179];
            tmp_called_name_101 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_101 == NULL)) {
                tmp_called_name_101 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_101 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 129;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 129;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_101);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 129;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[180];
            tmp_called_name_102 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_102 == NULL)) {
                tmp_called_name_102 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_102 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 130;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 130;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_102);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 130;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[181];
            tmp_called_name_103 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_103 == NULL)) {
                tmp_called_name_103 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_103 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 131;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 131;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_103);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 131;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[182];
            tmp_called_name_104 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_104 == NULL)) {
                tmp_called_name_104 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_104 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 132;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_99 = PyDict_Copy(mod_consts[29]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 132;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_104, tmp_kwargs_name_99);
            Py_DECREF(tmp_kwargs_name_99);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 132;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[183];
            tmp_called_name_105 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_105 == NULL)) {
                tmp_called_name_105 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_105 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 133;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_100 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 133;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_105, tmp_kwargs_name_100);
            Py_DECREF(tmp_kwargs_name_100);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 133;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[184];
            tmp_called_name_106 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_106 == NULL)) {
                tmp_called_name_106 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_106 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 134;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_101 = PyDict_Copy(mod_consts[185]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 134;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_106, tmp_kwargs_name_101);
            Py_DECREF(tmp_kwargs_name_101);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 134;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[186];
            tmp_called_name_107 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_107 == NULL)) {
                tmp_called_name_107 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_107 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 135;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_102 = PyDict_Copy(mod_consts[187]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 135;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_107, tmp_kwargs_name_102);
            Py_DECREF(tmp_kwargs_name_102);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 135;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[188];
            tmp_called_name_108 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_108 == NULL)) {
                tmp_called_name_108 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_108 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 136;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_103 = PyDict_Copy(mod_consts[50]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 136;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_108, tmp_kwargs_name_103);
            Py_DECREF(tmp_kwargs_name_103);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 136;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[189];
            tmp_called_name_109 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_109 == NULL)) {
                tmp_called_name_109 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_109 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 137;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_104 = PyDict_Copy(mod_consts[52]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 137;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_109, tmp_kwargs_name_104);
            Py_DECREF(tmp_kwargs_name_104);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 137;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[190];
            tmp_called_name_110 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_110 == NULL)) {
                tmp_called_name_110 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_110 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 138;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 138;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_110);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 138;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[191];
            tmp_called_name_111 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_111 == NULL)) {
                tmp_called_name_111 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_111 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 139;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_105 = PyDict_Copy(mod_consts[192]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 139;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_111, tmp_kwargs_name_105);
            Py_DECREF(tmp_kwargs_name_105);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 139;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[193];
            tmp_called_name_112 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_112 == NULL)) {
                tmp_called_name_112 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_112 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 140;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_106 = PyDict_Copy(mod_consts[192]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 140;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_112, tmp_kwargs_name_106);
            Py_DECREF(tmp_kwargs_name_106);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 140;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[194];
            tmp_called_name_113 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_113 == NULL)) {
                tmp_called_name_113 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_113 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 141;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_107 = PyDict_Copy(mod_consts[48]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 141;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_113, tmp_kwargs_name_107);
            Py_DECREF(tmp_kwargs_name_107);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 141;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[195];
            tmp_called_name_114 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_114 == NULL)) {
                tmp_called_name_114 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_114 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 142;

                goto dict_build_exception_1;
            }
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 142;
            tmp_dict_value_1 = CALL_FUNCTION_NO_ARGS(tmp_called_name_114);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 142;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[196];
            tmp_called_name_115 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_115 == NULL)) {
                tmp_called_name_115 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_115 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_108 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 143;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_115, tmp_kwargs_name_108);
            Py_DECREF(tmp_kwargs_name_108);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[197];
            tmp_called_name_116 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_116 == NULL)) {
                tmp_called_name_116 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_116 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 144;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_109 = PyDict_Copy(mod_consts[198]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 144;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_116, tmp_kwargs_name_109);
            Py_DECREF(tmp_kwargs_name_109);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 144;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[199];
            tmp_called_name_117 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_117 == NULL)) {
                tmp_called_name_117 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_117 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 145;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_110 = PyDict_Copy(mod_consts[24]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 145;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_117, tmp_kwargs_name_110);
            Py_DECREF(tmp_kwargs_name_110);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 145;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[200];
            tmp_called_name_118 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_118 == NULL)) {
                tmp_called_name_118 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_118 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 146;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_111 = PyDict_Copy(mod_consts[201]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 146;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_118, tmp_kwargs_name_111);
            Py_DECREF(tmp_kwargs_name_111);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 146;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[202];
            tmp_called_name_119 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_119 == NULL)) {
                tmp_called_name_119 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_119 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 147;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_112 = PyDict_Copy(mod_consts[32]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 147;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_119, tmp_kwargs_name_112);
            Py_DECREF(tmp_kwargs_name_112);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 147;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[203];
            tmp_called_name_120 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_120 == NULL)) {
                tmp_called_name_120 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_120 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_113 = PyDict_Copy(mod_consts[29]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 148;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_120, tmp_kwargs_name_113);
            Py_DECREF(tmp_kwargs_name_113);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[204];
            tmp_called_name_121 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_121 == NULL)) {
                tmp_called_name_121 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_121 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 149;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_114 = PyDict_Copy(mod_consts[149]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 149;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_121, tmp_kwargs_name_114);
            Py_DECREF(tmp_kwargs_name_114);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 149;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[205];
            tmp_called_name_122 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_122 == NULL)) {
                tmp_called_name_122 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_122 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 150;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_115 = PyDict_Copy(mod_consts[206]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 150;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_122, tmp_kwargs_name_115);
            Py_DECREF(tmp_kwargs_name_115);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 150;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[207];
            tmp_called_name_123 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

            if (unlikely(tmp_called_name_123 == NULL)) {
                tmp_called_name_123 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
            }

            if (tmp_called_name_123 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 151;

                goto dict_build_exception_1;
            }
            tmp_kwargs_name_116 = PyDict_Copy(mod_consts[78]);
            frame_12dd45c01af18592233b5ff461cc59cc->m_frame.f_lineno = 151;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_KEYARGS(tmp_called_name_123, tmp_kwargs_name_116);
            Py_DECREF(tmp_kwargs_name_116);
            if (tmp_dict_value_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 151;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_7, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_1;
        // Exception handling pass through code for dict_build:
        dict_build_exception_1:;
        Py_DECREF(tmp_assign_source_7);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[208], tmp_assign_source_7);
    }
    {
        PyObject *tmp_ass_subvalue_1;
        PyObject *tmp_expression_name_1;
        PyObject *tmp_subscript_name_1;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_ass_subscribed_1;
        PyObject *tmp_ass_subscript_1;
        tmp_expression_name_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_expression_name_1 == NULL)) {
            tmp_expression_name_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
        }

        if (tmp_expression_name_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
        tmp_tuple_element_1 = (PyObject *)&PyUnicode_Type;
        tmp_subscript_name_1 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_subscript_name_1, 0, tmp_tuple_element_1);
        tmp_tuple_element_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_tuple_element_1 == NULL)) {
            tmp_tuple_element_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
        }

        if (tmp_tuple_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto tuple_build_exception_1;
        }
        PyTuple_SET_ITEM0(tmp_subscript_name_1, 1, tmp_tuple_element_1);
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_subscript_name_1);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_ass_subvalue_1 = LOOKUP_SUBSCRIPT(tmp_expression_name_1, tmp_subscript_name_1);
        Py_DECREF(tmp_subscript_name_1);
        if (tmp_ass_subvalue_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
        tmp_ass_subscribed_1 = GET_STRING_DICT_VALUE(moduledict_rich$default_styles, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_ass_subscribed_1 == NULL)) {
            tmp_ass_subscribed_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_ass_subscribed_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_1);

            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_1 = mod_consts[208];
        tmp_result = SET_SUBSCRIPT(tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1);
        Py_DECREF(tmp_ass_subvalue_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_12dd45c01af18592233b5ff461cc59cc);
#endif
    popFrameStack();

    assertFrameObject(frame_12dd45c01af18592233b5ff461cc59cc);

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_12dd45c01af18592233b5ff461cc59cc);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_12dd45c01af18592233b5ff461cc59cc, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_12dd45c01af18592233b5ff461cc59cc->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_12dd45c01af18592233b5ff461cc59cc, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;

    return module_rich$default_styles;
    module_exception_exit:
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}

