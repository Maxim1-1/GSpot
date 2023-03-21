'use client'

import styled from 'styled-components'

export const List = styled.ul`
    position: relative;
    display: block;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    margin-top: 30px;

    margin-bottom: 40px;

    @media (min-width: 360px) {
        padding: 20px;
    }

    @media (min-width: 768px) {
        margin-bottom: 60px;
    }

    @media (min-width: 1200px) {
        margin-bottom: 0;
    }
`

export const ListItem = styled.li`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: stretch;
    padding-top: 15px;
    margin-top: 15px;
    border-top: 1px solid rgba(167, 130, 233, 0.06);
    position: relative;

    :first-child {
        margin-top: 0;
        padding-top: 0;
        border: none;
    }

    @media (min-width: 360px) {
        padding-top: 20px;
        margin-top: 20px;

        :first-child {
            margin-top: 0;
            padding-top: 0;
        }
    }
`

export const ListCover = styled.a`
    position: relative;
    display: block;
    border-radius: 6px;
    overflow: hidden;
    width: 90px;

    img {
        width: 100%;
        position: relative;
        z-index: 1;
        max-height: 150px;
        transition: 0.5s;
    }

    :hover img {
        opacity: 0.6;
    }

    @media (min-width: 576px) {
        width: 105px;
    }
`

export const ListWrap = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: calc(100% - 105px);

    @media (min-width: 576px) {
        width: calc(100% - 125px);
    }
`

export const ListTitle = styled.h3`
    width: 100%;
    margin-bottom: 10px;
    color: #fff;
    font-size: 16px;
    font-weight: 400;
    transition: 0.5s;

    :hover {
        color: #a782e9;
    }

    a {
        color: #fff;

        :hover {
            color: #a782e9;
        }
    }
`

export const ListPrice = styled.div`
    margin-top: auto;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    width: 100%;

    span {
        width: 100%;
        font-size: 24px;
        color: #fff;
        font-weight: 600;
        line-height: 100%;
        display: block;
    }

    s {
        font-size: 13px;
        color: #dbdada;
        margin-top: 7px;
        margin-right: 15px;
    }

    b {
        font-size: 13px;
        color: #fd6060;
        margin-top: 7px;
        margin-right: 15px;
        font-weight: 600;
    }
`

export const ListBuy = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 44px;
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    position: absolute;
    right: 0;
    bottom: 0;

    svg {
        stroke: #fff;
        width: 24px;
        height: auto;
    }

    :hover {
        background-color: #a782e9;
    }
`