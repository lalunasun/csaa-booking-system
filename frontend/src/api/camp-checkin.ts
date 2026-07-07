import { get, post } from '/@/utils/http/axios';
import axios from 'axios';
import { ADMIN_USER_TOKEN, BASE_URL } from '/@/store/constants';

enum URL {
  search = '/CSAA/campCheckin/search',
  signIn = '/CSAA/campCheckin/signIn',
  signOut = '/CSAA/campCheckin/signOut',
  summary = '/CSAA/admin/campCheckin/summary',
  importEnrollments = '/CSAA/admin/campCheckin/import',
  exportAttendance = '/CSAA/admin/campCheckin/export',
}

const searchApi = async (params: any) => get<any>({ url: URL.search, params, headers: {} });
const signInApi = async (data: any) => post<any>({ url: URL.signIn, data, headers: {} });
const signOutApi = async (data: any) => post<any>({ url: URL.signOut, data, headers: {} });
const summaryApi = async (params: any) => get<any>({ url: URL.summary, params, headers: {} });
const importEnrollmentsApi = async (data: any) =>
  post<any>({ url: URL.importEnrollments, data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const exportAttendanceApi = async (params: any) =>
  axios.get(`${BASE_URL}${URL.exportAttendance}`, {
    params,
    responseType: 'blob',
    headers: {
      ADMINTOKEN: localStorage.getItem(ADMIN_USER_TOKEN) || '',
    },
  });

export { searchApi, signInApi, signOutApi, summaryApi, importEnrollmentsApi, exportAttendanceApi };
