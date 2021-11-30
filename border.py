import math as m
def dot_con_check(m_dot ,neigh_dots, alpha, beta):
    #flats: Ax + By + Cz = 0  (A, B, C)
    upper_fl = ( 0, m.tan(beta + m.pi/6 ), 1 )
    lower_fl = ( 0, m.tan(beta - m.pi/6), 1 )
    right_fl = ( m.tan(alpha + m.pi/3  ), 0, 1)
    left_fl = ( m.tan(alpha - m.pi/3  ), 0, 1 )
    m_rho = [0]*4
    m_rho[0] = abs( upper_fl[0] * m_dot[0] + upper_fl[1] * m_dot[1] + upper_fl[2] * m_dot[2]) / ((upper_fl[0]**2 + upper_fl[1]**2 + upper_fl[2]**2)**0.5)
    m_rho[1] = abs( lower_fl[0] * m_dot[0] + lower_fl[1] * m_dot[1] + lower_fl[2] * m_dot[2] ) / ((lower_fl[0]**2 + lower_fl[1]**2 + lower_fl[2]**2)**0.5)
    m_rho[3] = abs( left_fl[0] * m_dot[0] + left_fl[1] * m_dot[1] + left_fl[2] * m_dot[2])/((left_fl[0]**2 + left_fl[1]**2 + left_fl[2]**2)**0.5)
    m_rho[2] = abs( right_fl[0] * m_dot[0] + right_fl[1] * m_dot[1] + right_fl[2] * m_dot[2])/((right_fl[0]**2 + right_fl[1]**2 + right_fl[2]**2)**0.5)
    for dot in neigh_dots:
        if (upper_fl[0]*m_dot[0] + upper_fl[1]*m_dot[1] + upper_fl[2]*m_dot[2]) < 0:
        if (upper_fl[0]*m_dot[0] + upper_fl[1]*m_dot[1] + upper_fl[2]*m_dot[2])*(upper_fl[0]*m_dot[0] + upper_fl[1]*m_dot[1] + upper_fl[2]*m_dot[2]) < 0:
        x_bord = (m_dot[0] - dot[])