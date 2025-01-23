import { format, parseISO } from 'date-fns';

export const formatDate = (dateString, formatString = 'yyyy-MM-dd') => {
  const date = parseISO(dateString);
  return format(date, formatString);
};
